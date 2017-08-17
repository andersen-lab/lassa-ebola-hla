import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches

plt.style.use("seaborn")

MHC_Class_I = ["HLA-A", "HLA-B", "HLA-C"]

# Calculate allele counts
df = pd.read_csv("../Genotype_calls.csv", na_values="-")
df = df.set_index("individual")
df = df.apply(lambda x:x.str.rstrip()) # Remove trailing whitespaces

# EVD
list_of_alleles = pd.DataFrame(columns=["MHC Class", "No. of Obs Alleles", "No. of Total Alleles", "No. of Individuals", "Allele_Count", "Allelic_Frequency", "Allele"])
# a = df[df["Status "]=="EVD"][df.columns.values[3:]].stack().value_counts(
a = df[df.columns.values[3:]].stack().value_counts()
list_of_alleles["Allele_Count"] = a.values
list_of_alleles["Allele"] = a.index.values
freq = []
individuals = []
for i in list_of_alleles.index:
    hla = list_of_alleles.ix[i]["Allele"].split("*")[0]
    _sum = df[df.columns[(df.columns.values == hla) | (df.columns.values == hla+".1")]].stack().dropna().value_counts().sum()
    freq.append(list_of_alleles.ix[i]["Allele_Count"]/_sum)
    if hla+".1" in df.columns.tolist():
        _ind = df[(~df[hla].isnull()) | (~df[hla+".1"].isnull())].shape[0]
    else:
        _ind = df[(~df[hla].isnull())].shape[0]
    individuals.append(_ind)
list_of_alleles["Allelic_Frequency"] = freq
list_of_alleles = list_of_alleles.set_index("Allele")
list_of_alleles["Gene"] = ["HLA-"+i[0] for i in list_of_alleles.index.str.split("*")]
list_of_alleles["No. of Individuals"] = individuals
list_of_alleles["No. of Obs Alleles"] = list_of_alleles["Gene"].apply(lambda x: list_of_alleles[list_of_alleles["Gene"]==x].shape[0])
list_of_alleles["No. of Total Alleles"] = list_of_alleles["Gene"].apply(lambda x: list_of_alleles[list_of_alleles["Gene"]==x]["Allele_Count"].sum())
list_of_alleles["MHC Class"] = list_of_alleles["Gene"].apply(lambda x: "MHC-I" if x in MHC_Class_I else "MHC-II")
list_of_alleles = list_of_alleles.sort_values(["Gene", "Allele_Count"], ascending=[True, False])
list_of_alleles.to_csv("../allele_frequencies.csv")


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
        
