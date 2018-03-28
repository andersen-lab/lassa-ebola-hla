import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches
from scipy.stats import fisher_exact
import statsmodels.stats.multitest as smm
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.style.use("seaborn")

def get_list_of_alleles(df):
    allelesdf = pd.DataFrame(columns=["MHC Class", "No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals", "Allele_Count", "Allelic_Frequency", "Allele"])    
    a = df[df.columns.values[3:]].stack().value_counts()
    allelesdf["Allele_Count"] = a.values
    allelesdf["Allele"] = a.index.values
    freq = []
    individuals = []
    for i in allelesdf.index:
        hla = allelesdf.ix[i]["Allele"].split("*")[0]
        # _sum = df[df.columns[(df.columns.values == hla) | (df.columns.values == hla+".1")]].stack().dropna().value_counts().sum()
        _sum = df.shape[0] * 2
        freq.append(allelesdf.ix[i]["Allele_Count"]/_sum)
        if hla+".1" in df.columns.tolist():
            _ind = df[(~df[hla].isnull()) | (~df[hla+".1"].isnull())].shape[0]
        else:
            _ind = df[(~df[hla].isnull())].shape[0]
        individuals.append(_ind)
    allelesdf["Allelic_Frequency"] = freq
    allelesdf = allelesdf.set_index("Allele")
    allelesdf["Gene"] = ["HLA-"+i[0] for i in allelesdf.index.str.split("*")]
    allelesdf["No. of Individuals"] = individuals
    allelesdf["No. of Obs Alleles"] = allelesdf["Gene"].apply(lambda x: allelesdf[allelesdf["Gene"]==x].shape[0])
    allelesdf["No. of Total Alleles"] = allelesdf["Gene"].apply(lambda x: allelesdf[allelesdf["Gene"]==x]["Allele_Count"].sum())
    allelesdf["MHC Class"] = allelesdf["Gene"].apply(lambda x: "MHC-I" if x in MHC_Class_I else "MHC-II")
    allelesdf = allelesdf.sort_values(["Gene", "Allele_Count"], ascending=[True, False])
    return allelesdf

MHC_Class_I = ["HLA-A", "HLA-B", "HLA-C"]

# Calculate allele counts
df = pd.read_csv("../Genotype_calls.csv", na_values="-")
df.columns = df.columns.str.rstrip()
df["ID"] = df["ID"].str.replace("-", "").str.replace("_", "").astype(str)
df["Status"] = df["Status"].astype(str).apply(lambda x: x.rstrip())
# df["Subject"] = df["Subject"].astype(str)
df = df.set_index("ID")
df = df.apply(lambda x:x.str.rstrip()) # Remove trailing whitespaces

for i in df.columns:
    df.loc[df[i].str.contains("NA", na=False), i] = np.nan

list_of_alleles = get_list_of_alleles(df)
list_of_alleles.to_csv("../allele_frequencies.csv")

# Total obs alleles
obs_total = list_of_alleles.groupby("Gene").mean()
obs_total[["No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals"]].to_csv("../Obs_Total_alleles.csv")

# Grouped alleles
evddf = get_list_of_alleles(df[df["Status"]=="EBOV"])
evd_total = evddf.groupby("Gene").mean()
evd_total = evd_total[["No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals"]]
evd_total.columns = evd_total.columns.map(lambda x: str(x).replace("No. of ", "").replace(" ", "_")+"_EBOV")

lasvdf = get_list_of_alleles(df[df["Status"]=="LASV"])
lasv_total = lasvdf.groupby("Gene").mean()
lasv_total = lasv_total[["No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals"]]
lasv_total.columns = lasv_total.columns.map(lambda x: str(x).replace("No. of ", "").replace(" ","_")+"_LASV")

ctrldf = get_list_of_alleles(df[df["Status"]=="Control"])
ctrl_total = ctrldf.groupby("Gene").mean()
ctrl_total = ctrl_total[["No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals"]]
ctrl_total.columns = ctrl_total.columns.map(lambda x: str(x).replace("No. of ", "").replace(" ","_")+"_CTRL")

evd_total.join(lasv_total).join(ctrl_total).to_csv("../Obs_Total_alleles_grouped.csv")

# Calculate differences between ebola and control
# Contingency table is
#        | evd | ctrl |
# allele |     |      |
# other  |     |      |

all = evddf.index.tolist()
all.extend(ctrldf.index.tolist())
all = list(set(all))
evd_ctrl_df = pd.DataFrame(index=all, columns=["EBOV Allele Count", "EBOV Allele Freq", "Control Allele Count", "Control Allele Freq", "pval", "corrected pval"])
rows = {
    "evdac": [],
    "evdfreq": [],
    "ctrlac": [],
    "ctrlfreq": [],
    "pval": []
}
for i in all:
    evd = [0, 0]
    ctrl = [0, 0]
    if i in ctrldf.index:
        ctrl = [ctrldf.ix[i, "Allele_Count"], ctrldf.ix[i, "Allelic_Frequency"]]
    if i in evddf.index:
        evd = [evddf.ix[i, "Allele_Count"], evddf.ix[i, "Allelic_Frequency"]]
    total = df.shape[0] * 2
    oddsratio, pvalue = fisher_exact([[evd[0], ctrl[0]],[(df[df["Status"]=="EBOV"].shape[0]*2)-evd[0], (df[df["Status"]=="Control"].shape[0]*2)-ctrl[0]]])
    rows["evdac"].append(evd[0])
    rows["evdfreq"].append(evd[1])
    rows["ctrlac"].append(ctrl[0])
    rows["ctrlfreq"].append(ctrl[1])
    rows["pval"].append(pvalue)
t = smm.multipletests(rows["pval"], alpha = 0.01, method="fdr_bh")
evd_ctrl_df["EBOV Allele Count"] = rows["evdac"]
evd_ctrl_df["EBOV Allele Freq"] = rows["evdfreq"]
evd_ctrl_df["Control Allele Count"] = rows["ctrlac"]
evd_ctrl_df["Control Allele Freq"] = rows["ctrlfreq"]
evd_ctrl_df["pval"] = rows["pval"]
evd_ctrl_df["corrected pval"] = t[1]
evd_ctrl_df["pass fdr test"] = t[0]
evd_ctrl_df.to_csv("../EBOV_vs_Control.csv")

all = lasvdf.index.tolist()
all.extend(ctrldf.index.tolist())
all = list(set(all))
lasv_ctrl_df = pd.DataFrame(index=all, columns=["LASV Allele Count", "LASV Allele Freq", "Control Allele Count", "Control Allele Freq", "pval", "corrected pval"])
rows = {
    "lasvac": [],
    "lasvfreq": [],
    "ctrlac": [],
    "ctrlfreq": [],
    "pval": []
}
for i in all:
    lasv = [0, 0]
    ctrl = [0, 0]
    if i in ctrldf.index:
        ctrl = [ctrldf.ix[i, "Allele_Count"], ctrldf.ix[i, "Allelic_Frequency"]]
    if i in lasvdf.index:
        lasv = [lasvdf.ix[i, "Allele_Count"], lasvdf.ix[i, "Allelic_Frequency"]]
    total = df.shape[0] * 2
    oddsratio, pvalue = fisher_exact([[lasv[0], ctrl[0]],[(df[df["Status"]=="LASV"].shape[0]*2), (df[df["Status"]=="Control"].shape[0]*2)]])
    rows["lasvac"].append(lasv[0])
    rows["lasvfreq"].append(lasv[1])
    rows["ctrlac"].append(ctrl[0])
    rows["ctrlfreq"].append(ctrl[1])
    rows["pval"].append(pvalue)
t = smm.multipletests(rows["pval"], alpha = 0.01, method="fdr_bh")
lasv_ctrl_df["LASV Allele Count"] = rows["lasvac"]
lasv_ctrl_df["LASV Allele Freq"] = rows["lasvfreq"]
lasv_ctrl_df["Control Allele Count"] = rows["ctrlac"]
lasv_ctrl_df["Control Allele Freq"] = rows["ctrlfreq"]
lasv_ctrl_df["pval"] = rows["pval"]
lasv_ctrl_df["corrected pval"] = t[1]
lasv_ctrl_df["pass fdr test"] = t[0]
lasv_ctrl_df.to_csv("../LASV_vs_Control.csv")

collateddf = evd_ctrl_df.drop(["pval", "corrected pval", "pass fdr test"], axis = 1)
collateddf = collateddf.join(lasv_ctrl_df.drop(["pval", "corrected pval", "pass fdr test", "Control Allele Count", "Control Allele Freq"], axis = 1), rsuffix="LASV", how="outer")
collateddf.fillna(0).to_csv("../EBOV_LASV_Control.csv")
collateddf = collateddf.fillna(0)

fc = collateddf.columns[collateddf.columns.str.contains("Freq")].values
for i in collateddf.index:
    dflag = True
    for j in fc:
        if collateddf.ix[i][j] >= 0.05:
            dflag = False
    if dflag:
        collateddf = collateddf.drop(i)
collateddf.to_csv("../EBOV_LASV_Control_0.05.csv")

e = collateddf[collateddf["EBOV Allele Freq"] >= 0.05].index.tolist()
l = collateddf[collateddf["LASV Allele Freq"] >= 0.05].index.tolist()
c = collateddf[collateddf["Control Allele Freq"] >= 0.05].index.tolist()

m = max([len(e), len(l), len(c)])
e.extend([""]*(m-len(e)))
l.extend([""]*(m-len(l)))
c.extend([""]*(m-len(c)))

t = pd.DataFrame()
t["EBOV"] = e
t["LASV"] = l
t["Control"] = c
t.to_csv("../grouped_alleles.csv")

d = collateddf[fc] > 0.05
myColors = ("#FFFFFF","#4682b4")
cmap = LinearSegmentedColormap.from_list('Custom', myColors, len(myColors))
fig, ax = plt.subplots(figsize=(8,20))
ax = sns.heatmap(d, cmap=cmap, linewidths=.1, linecolor='lightgray', ax = ax)
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0, 1])
colorbar.set_ticklabels(['Absent', 'Present'])
ax.set_xlabel('Allele')
_, labels = plt.yticks()
plt.setp(labels, rotation=0)
plt.tight_layout()
plt.savefig("../img/grouped.png")
plt.clf()
plt.close()

# Counts plot
ax = list_of_alleles.groupby(["Gene"]).mean()[["No. of Individuals", "No. of Obs Alleles", "No. of Total Alleles"]].plot(kind="bar")
ax.set_title("Counts per HLA Gene")
ax.set_ylabel("Count")
plt.tight_layout()
plt.savefig("../img/counts.png")
plt.clf()
plt.close()

# Plot Alleles with Frequency >= 5%
fig, ax = plt.subplots(figsize=(20,10))
c = list_of_alleles[list_of_alleles["Allelic_Frequency"]>0.05]["Allelic_Frequency"].sort_values(ascending=False)
c.plot(kind="bar", ax = ax)
pos = [c.index.get_loc(i) for i in c.index[c.index.str.contains("@")]]
for i in pos:
    ax.get_xticklabels()[i].set_color("red")
ax.set_title("Frequencies of Alleles(>5%)")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("../img/allelic_frequency.png")
plt.clf()
plt.close()

# Generate Markdown Table for README.md
print("Copy markdown table into README.md")
c = list_of_alleles[list_of_alleles["Allelic_Frequency"]>0.05].sort_values(["Gene", "Allelic_Frequency"],ascending=[True, False])
c1 = "MHC-I"
c2 = "MHC-II"
print("\n")
print("| "+c1+"| | |"+c2+"| | |")
print("| Gene | Allele | Allelic Frequency | Gene | Allele | Allelic Frequency |")
print("| --- | --- | --- | --- | --- | --- |")
c1 = c[c["MHC Class"] == c1]
c2 = c[c["MHC Class"] == c2]
for i in range(0, max(len(c1), len(c2))):
    l = ""
    if i < len(c1):
        _ = c1.index[i]
        l+="| "+c1["Gene"][_]+" | "+str(_)+" | "+ str(round(c1["Allelic_Frequency"][_]*100)/100)
    else:
        l+="| | | "
    if i <len(c2):
        _ = c2.index[i]
        l+="| "+c2["Gene"][_]+" | "+str(_)+" | "+ str(round(c2["Allelic_Frequency"][_]*100)/100)+" | "
    print(l)
