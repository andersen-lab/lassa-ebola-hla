*Summary: HLA genotyping of Lassa and Ebola patients. [Data here](https://github.com/andersen-lab/lassa-ebola-hla).*

In an effort to increase our understanding of the immune response to Lassa virus (LASV) and Ebola virus (EBOV), we are typing the human leukocyte antigen (HLA) genes from Lassa and Ebola patients, as well as healthy individuals.

We perform the HLA typing using the Illumina TruSight HLA Sequencing Panel, which allows for the isolation and amplification of 11 HLA loci (Class I HLA-A, -B, -C; Class II HLA-DRB1/3/4/5, -DQA1, -DQB1, -DPA1, -DPB1) using long range PCR. Amplicons are used to produce libraries using the Illumina Nextera protocol and sequenced on the Illumina MiSeq platform. HLA-optimized software is used to analyze sequence data, produce consensus sequences and compare them to to the IMGT/HLA database for HLA genotype assignments.

To date, we have sequenced and genotyped 39 PBMC samples from Lassa and Ebola patients (23 Ebola + 22 Lassa), resulting in a total of 808 alleles sequenced ([Obs_Total_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles.csv)). Ebola patients yielded 109 unique alleles and Lassa patients yielded 118 unique alleles ([Obs_Total_alleles_grouped.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles_grouped.csv)). As part of a collaboration with the Broad Institute, we also have HLA types from another hundred Sierra Leonean individuals. Together with Illumina, we are planning to type another couple of hundred individuals by the end of 2017 and will release the data here once generated - stay tuned.

So far, the data suggest the presence of a high number of novel alleles - that is alleles with no reference in the IMGT/HLA database ([novel_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/novel_alleles.csv)). Six of these are found in the Class II HLA loci. The DPA1 loci has the highest number with 3 novel alleles. A novel allele of particular interest is the presence of a nonsynonymous mutation in the start codon (ATG to ACG) of the DPA1 loci (DPA1*03:01@2). 

A comprehensive list of the 143 HLA alleles sequenced and their frequencies is presented in ([allele_frequencies.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/allele_frequencies.csv))). 

Thus far, the results of this project have contributed in the efforts to characterize the under-represented West African population in the IMGT/HLA database, and most importantly, these results may shed light in understanding the contribution of specific HLA genotypes in association with outcomes of hemorrhagic fever infection in the West African population.

### Allelic Frequencies(>5%)

| MHC-I |          |                   | MHC-II   |             |                   |
| ---   | ---      |               --- | ---      | ---         |               --- |
| Gene  | Allele   | Allelic Frequency | Gene     | Allele      | Allelic Frequency |
| HLA-A | A*030101 |              0.12 | HLA-DPA1 | DPA1*020101 |              0.29 |
| HLA-A | A*300101 |              0.12 | HLA-DPA1 | DPA1*020108 |              0.21 |
| HLA-A | A*300201 |              0.11 | HLA-DPA1 | DPA1*020202 |              0.17 |
| HLA-A | A*020101 |               0.1 | HLA-DPA1 | DPA1*0301   |              0.09 |
| HLA-A | A*740101 |               0.1 | HLA-DPA1 | DPA1*0301@2 |              0.08 |
| HLA-A | A*230101 |              0.08 | HLA-DPA1 | DPA1*0207@4 |              0.07 |
| HLA-A | A*330301 |              0.07 | HLA-DPA1 | DPA1*010301 |              0.06 |
| HLA-A | A*680101 |              0.06 | HLA-DPB1 | DPB1*010101 |              0.39 |
| HLA-A | A*340201 |              0.06 | HLA-DPB1 | DPB1*10501  |              0.13 |
| HLA-B | B*530101 |              0.13 | HLA-DPB1 | DPB1*010102 |               0.1 |
| HLA-B | B*350101 |              0.12 | HLA-DPB1 | DPB1*1701   |              0.09 |
| HLA-B | B*420101 |              0.12 | HLA-DPB1 | DPB1*8501   |              0.07 |
| HLA-B | B*580101 |              0.08 | HLA-DPB1 | DPB1*4001   |              0.06 |
| HLA-B | B*070201 |              0.07 | HLA-DQA1 | DQA1*050501 |              0.22 |
| HLA-B | B*150301 |              0.06 | HLA-DQA1 | DQA1*010201 |               0.2 |
| HLA-C | C*040101 |              0.18 | HLA-DQA1 | DQA1*040101 |               0.2 |
| HLA-C | C*170101 |              0.13 | HLA-DQA1 | DQA1*030301 |              0.13 |
| HLA-C | C*030202 |              0.12 | HLA-DQA1 | DQA1*010202 |              0.08 |
| HLA-C | C*160101 |              0.09 | HLA-DQA1 | DQA1*040102 |              0.07 |
| HLA-C | C*021001 |              0.08 | HLA-DQA1 | DQA1*020101 |              0.06 |
| HLA-C | C*070201 |              0.06 | HLA-DQB1 | DQB1*031901 |               0.2 |
| HLA-C | C*0718   |              0.06 | HLA-DQB1 | DQB1*040201 |              0.19 |
|       |          |                   | HLA-DQB1 | DQB1*020201 |              0.13 |
|       |          |                   | HLA-DQB1 | DQB1*060901 |              0.09 |
|       |          |                   | HLA-DQB1 | DQB1*050101 |              0.08 |
|       |          |                   | HLA-DQB1 | DQB1*050201 |              0.07 |
|       |          |                   | HLA-DQB1 | DQB1*030101 |              0.07 |
|       |          |                   | HLA-DQB1 | DQB1*030201 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*030201 |               0.2 |
|       |          |                   | HLA-DRB1 | DRB1*130201 |              0.14 |
|       |          |                   | HLA-DRB1 | DRB1*080401 |              0.08 |
|       |          |                   | HLA-DRB1 | DRB1*160201 |              0.07 |
|       |          |                   | HLA-DRB1 | DRB1*110102 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*090102 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*070101 |              0.06 |
|       |          |                   | HLA-DRB1 | DRB1*110201 |              0.06 |
|       |          |                   | HLA-DRB3 | DRB3*010102 |              0.43 |
|       |          |                   | HLA-DRB3 | DRB3*020201 |               0.3 |
|       |          |                   | HLA-DRB3 | DRB3*030101 |              0.27 |
|       |          |                   | HLA-DRB4 | DRB4*010301 |              0.57 |
|       |          |                   | HLA-DRB4 | DRB4*010101 |              0.43 |
|       |          |                   | HLA-DRB5 | DRB5*02@7   |              0.71 |
|       |          |                   | HLA-DRB5 | DRB5*02@9   |              0.14 |
|       |          |                   | HLA-DRB5 | DRB5*010101 |              0.14 |

\*Novel Alleles highlighted in <span style="color: red;">RED</span>.

![Allele Frequency](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/allelic_frequency.png)

![Counts per HLA Gene](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/counts.png)
