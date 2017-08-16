*Summary: HLA genotyping of Lassa and Ebola patients. [Data here](https://github.com/andersen-lab/lassa-ebola-hla).*

In an effort to increase our understanding of the immune response to Lassa virus (LASV) and Ebola virus (EBOV), we are typing the human leukocyte antigen (HLA) genes from Lassa and Ebola patients, as well as healthy individuals.

We perform the HLA typing using the Illumina TruSight HLA Sequencing Panel, which allows for the isolation and amplification of 11 HLA loci (Class I HLA-A, -B, -C; Class II HLA-DRB1/3/4/5, -DQA1, -DQB1, -DPA1, -DPB1) using long range PCR. Amplicons are used to produce libraries using the Illumina Nextera protocol and sequenced on the Illumina MiSeq platform. HLA-optimized software is used to analyze sequence data, produce consensus sequences and compare them to to the IMGT/HLA database for HLA genotype assignments.

To date, we have sequenced and genotyped 39 PBMC samples from Lassa and Ebola patients (22 Ebola + 17 Lassa), resulting in a total of 702 alleles sequenced ([Obs_Total_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles.csv)). Ebola patients yielded 109 unique alleles and Lassa patients yielded 108 unique alleles ([Obs_Total_alleles_grouped.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles_grouped.csv)). As part of a collaboration with the Broad Institute, we also have HLA types from another hundred Sierra Leonean individuals. Together with Illumina, we are planning to type another couple of hundred individuals by the end of 2017 and will release the data here once generated - stay tuned.

So far, the data suggest the presence of a high number of novel alleles - that is alleles with no reference in the IMGT/HLA database ([novel_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/novel_alleles.csv)). Six of these are found in the Class II HLA loci. The DPA1 loci has the highest number with 3 novel alleles. A novel allele of particular interest is the presence of a nonsynonymous mutation in the start codon (ATG to ACG) of the DPA1 loci (DPA1*03:01@2). 

A comprehensive list of the HLA alleles sequenced and their frequencies in the Ebola and Lassa groups is presented in ([list_of_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/list_of_alleles.csv)). 

#### Allele Frequencies in EVD vs LASV patients.
\*Novel Alleles highlighted in <span style="color: red;">RED</span>.

![Allele Frequency](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/allele_frequency.png)
