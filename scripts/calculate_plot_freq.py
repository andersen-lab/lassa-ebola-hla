import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches
import scipy
import statsmodels.stats.multitest as smm

plt.style.use("seaborn")

# Calculate allele counts
df = pd.read_csv("../Genotype_calls.csv", na_values="-")
df = df.set_index("individual")
df = df.apply(lambda x:x.str.rstrip()) # Remove trailing whitespaces

# EVD
list_of_alleles_EVD = pd.DataFrame(columns=["Count_EVD", "Allele_Frequency_EVD", "HLA"])
a = df[df["Status "]=="EVD"][df.columns.values[3:]].stack().value_counts()
list_of_alleles_EVD["Count_EVD"] = a.values
list_of_alleles_EVD["HLA"] = a.index.values
freq = []
ebola_df = df[df["Status "] == "EVD"]
for i in list_of_alleles_EVD.index:
    hla = list_of_alleles_EVD.ix[i]["HLA"].split("*")[0]
    _sum = ebola_df[ebola_df.columns[(ebola_df.columns.values == hla) | (ebola_df.columns.values == hla+".1")]].stack().dropna().value_counts().sum()
    freq.append(list_of_alleles_EVD.ix[i]["Count_EVD"]/_sum)
list_of_alleles_EVD["Allele_Frequency_EVD"] = freq
list_of_alleles_EVD = list_of_alleles_EVD.set_index("HLA")
[]
# LASV
list_of_alleles_LASV = pd.DataFrame(columns=["Count_LASV", "Allele_Frequency_LASV", "HLA"])
a = df[df["Status "]=="LASV"][df.columns.values[3:]].stack().value_counts()
list_of_alleles_LASV["Count_LASV"] = a.values
list_of_alleles_LASV["HLA"] = a.index.values
freq = []
ebola_df = df[df["Status "] == "LASV"]
for i in list_of_alleles_LASV.index:
    hla = list_of_alleles_LASV.ix[i]["HLA"].split("*")[0]
    _sum = ebola_df[ebola_df.columns[(ebola_df.columns.values == hla) | (ebola_df.columns.values == hla+".1")]].stack().dropna().value_counts().sum()
    freq.append(list_of_alleles_LASV.ix[i]["Count_LASV"]/_sum)
list_of_alleles_LASV["Allele_Frequency_LASV"] = freq
list_of_alleles_LASV = list_of_alleles_LASV.set_index("HLA")

c = pd.concat([list_of_alleles_EVD, list_of_alleles_LASV], axis = 1).fillna(0)
c["Total_Allele_frequency"] = c["Allele_Frequency_EVD"]+c["Allele_Frequency_LASV"]
c = c.sort_values("Total_Allele_frequency", ascending=False) # Concatenated dataframe

# Plot 
fig, ax = plt.subplots(figsize=(20,10))
c[["Allele_Frequency_EVD", "Allele_Frequency_LASV"]].plot(kind="bar", ax = ax)
pos = [c.index.get_loc(i) for i in c.index[c.index.str.contains("@")]] # Unique Alleles contain an @ symbol
for i in pos:
    ax.get_xticklabels()[i].set_color("red")
ax.set_title("Allele Frequencies EVD vs LASV Patients")
ax.set_xlabel("HLA Alleles")
ax.set_ylabel("Allele Frequencies")
plt.tight_layout()
plt.savefig("../img/allele_frequency.png")
plt.clf()
plt.close()

# Test for statistical significance in difference of counts for EVD vs LASV patients.
evd_total = c["Count_EVD"].sum()
lasv_total = c["Count_LASV"].sum()
pvalues = []
for i in c.index:
    _ = [[c.ix[i]["Count_EVD"], c.ix[i]["Count_LASV"]], [evd_total, lasv_total]]
    oddsratio, pval = scipy.stats.fisher_exact(_)
    pvalues.append(pval)
corrected_pval = smm.multipletests(pvalues, method="fdr_bh", alpha=0.05)
c["pval"] = corrected_pval[1]
print("Number of HLA types that have significant differences in EVD vs LASV patients: "+str(list(corrected_pval[0]).count(True)))

