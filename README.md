*Summary: HLA genotyping of Lassa and Ebola patients from Sierra Leone. [Data here](https://github.com/andersen-lab/lassa-ebola-hla).*

In an effort to increase our understanding of the immune response to Lassa virus (LASV) and Ebola virus (EBOV), we are typing the human leukocyte antigen (HLA) genes from Lassa and Ebola patients, as well as healthy individuals.

We perform the HLA typing using the Illumina TruSight HLA Sequencing Panel, which allows for the isolation and amplification of 11 HLA loci (Class I HLA-A, -B, -C; Class II HLA-DRB1/3/4/5, -DQA1, -DQB1, -DPA1, -DPB1) using long range PCR. Amplicons are used to produce libraries using the Illumina Nextera protocol and sequenced on the Illumina MiSeq platform. HLA-optimized software is used to analyze sequence data, produce consensus sequences and compare them to to the IMGT/HLA database for HLA genotype assignments.

To date, we have sequenced and genotyped 80 PBMC samples from Lassa and Ebola patients (53 Ebola + 27 Lassa), resulting in a total of 1436 alleles sequenced ([Obs_Total_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles.csv)). Ebola patients yielded 161 unique alleles and Lassa patients yielded 135 unique alleles ([Obs_Total_alleles_grouped.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles_grouped.csv)). As part of a collaboration with the Broad Institute, we also have HLA types from another hundred Sierra Leonean individuals. Together with Illumina, we are currently genotyping over 140 new  individuals, and will release the data here once we generate it - stay tuned.

So far, the data suggest the presence of a high number of novel alleles - that is alleles with no reference in the IMGT/HLA database ([novel_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/novel_alleles.csv)). Eleven of these are found in the Class II HLA loci. The DPA1 loci has the highest number with 6 novel alleles. A novel allele of particular interest is the presence of a nonsynonymous mutation in the start codon (ATG to ACG) of the DPA1 loci (DPA1*03:01@2).

A comprehensive list of the 181 HLA alleles sequenced and their frequencies is presented in ([allele_frequencies.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/allele_frequencies.csv))).

Thus far, the results of this project have contributed in the efforts to characterize the under-represented West African population in the IMGT/HLA database, and most importantly, these results may shed light in understanding the contribution of specific HLA genotypes in association with outcomes of hemorrhagic fever infection in the West African population.


#### Allelic Frequencies(>5%)

| MHC-I |          |                   | MHC-II   |             |                   |
| ---   | ---      |               --- | ---      | ---         |               --- |
| Gene  | Allele   | Allelic Frequency | Gene     | Allele      | Allelic Frequency |
| HLA-A | A*300101 |              0.13 | HLA-DPA1 | DPA1*020101 |              0.23 |
| HLA-A | A*300201 |              0.09 | HLA-DPA1 | DPA1*020202 |              0.22 |
| HLA-A | A*020101 |              0.09 | HLA-DPA1 | DPA1*020108 |              0.18 |
| HLA-A | A*030101 |              0.09 | HLA-DPA1 | DPA1*0301   |              0.09 |
| HLA-A | A*740101 |              0.08 | HLA-DPA1 | DPA1*010301 |              0.08 |
| HLA-A | A*230101 |              0.08 | HLA-DPA1 | DPA1*0207@4 |              0.07 |
| HLA-A | A*340201 |              0.07 | HLA-DPA1 | DPA1*0301@2 |              0.06 |
| HLA-A | A*330301 |              0.06 | HLA-DPB1 | DPB1*010101 |              0.41 |
| HLA-B | B*350101 |              0.12 | HLA-DPB1 | DPB1*10501  |               0.1 |
| HLA-B | B*530101 |              0.12 | HLA-DPB1 | DPB1*8501   |              0.07 |
| HLA-B | B*420101 |              0.09 | HLA-DPB1 | DPB1*010102 |              0.07 |
| HLA-B | B*580101 |              0.07 | HLA-DPB1 | DPB1*130101 |              0.06 |
| HLA-B | B*070201 |              0.06 | HLA-DQA1 | DQA1*050501 |              0.22 |
| HLA-C | C*040101 |              0.19 | HLA-DQA1 | DQA1*040101 |              0.19 |
| HLA-C | C*160101 |              0.14 | HLA-DQA1 | DQA1*010201 |              0.19 |
| HLA-C | C*170101 |              0.11 | HLA-DQA1 | DQA1*030301 |              0.11 |
| HLA-C | C*030202 |              0.08 | HLA-DQA1 | DQA1*010202 |              0.06 |
| HLA-C | C*0718   |              0.06 | HLA-DQA1 | DQA1*020101 |              0.06 |
| HLA-C | C*070201 |              0.06 | HLA-DQB1 | DQB1*040201 |              0.19 |
|       |          |                   | HLA-DQB1 | DQB1*031901 |              0.18 |
|       |          |                   | HLA-DQB1 | DQB1*020201 |              0.12 |
|       |          |                   | HLA-DQB1 | DQB1*050101 |              0.12 |
|       |          |                   | HLA-DQB1 | DQB1*030101 |              0.07 |
|       |          |                   | HLA-DQB1 | DQB1*060901 |              0.06 |
|       |          |                   | HLA-DQB1 | DQB1*050201 |              0.06 |
|       |          |                   | HLA-DQB1 | DQB1*060201 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*030201 |               0.2 |
|       |          |                   | HLA-DRB1 | DRB1*130201 |              0.11 |
|       |          |                   | HLA-DRB1 | DRB1*110102 |              0.07 |
|       |          |                   | HLA-DRB1 | DRB1*1304   |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*160201 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*080401 |              0.06 |
|       |          |                   | HLA-DRB3 | DRB3*010102 |              0.31 |
|       |          |                   | HLA-DRB3 | DRB3*020201 |              0.31 |
|       |          |                   | HLA-DRB3 | DRB3*030101 |              0.14 |
|       |          |                   | HLA-DRB4 | DRB4*010101 |              0.08 |
|       |          |                   | HLA-DRB4 | DRB4*010301 |              0.06 |

\*Novel Alleles highlighted in <span style="color: red;">RED</span>.

![Allele Frequency](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/allelic_frequency.png)

![Counts per HLA Gene](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/counts.png)

**Disclaimer**. Please note that this data is still based on work in progress and should be considered preliminary. If you intend to include any of these data in publications, please let us know – otherwise please feel free to download and use without restrictions. We have shared this data with the hope that people will download and use it, as well as scrutinize it so we can improve our methods and analyses. Please contact us if you have any questions or comments – we’ll buy beers for #ResearchParasites that spot flaws and faults in the data and come up with improvements!

---
**Andersen Lab**
The Scripps Research Institute
La Jolla, CA, USA
[data@andersen-lab.com](mailto:data@andersen-lab.com)
