# HLA Genotype Sequencing of Hemorrhagic Fever Survivors using Illumina TruSight HLA v2 Sequencing Panel

In an effort to increase our understanding of the immune responses to viruses responsible of causing severe hemorrhagic illnesses such as Lassa virus (LASV) and Ebola virus (EBOV) our lab, along with numerous researchers around the world, is currently collaborating in the Hemorrhagic Fever Consortium. Our work focuses in genotyping the human leukocyte antigen (HLA) gene region from Lassa fever and Ebola virus disease survivors, using the Illumina TruSight HLA Sequencing Panel.

Briefly, this technology allows the isolation and amplification of 11 HLA loci (Class I HLA-A, -B, -C; Class II HLA-DRB1/3/4/5, -DQA1, -DQB1, -DPA1, -DPB1) using long range PCR. Amplicons are used to produce libraries using the Illumina Nextera protocol and sequenced on the Illumina MiSeq platform. HLA-optimized software is used to analyze sequence data, produce consensus sequences and compare them to to the IMGT/HLA database for HLA genotype assignation.

To date, we have sequenced and genotyped 39 PBMC DNA samples from Lassa fever (LF) and Ebola virus disease (EVD) patients (22 EVD + 17 LASV), resulting in a total of 702 alleles sequenced ([Obs_Total_alleles.csv](Obs_Total_alleles.csv)). EVD survivors (n=22) yielded 109 unique alleles and LF survivors (n=17) yielded 108 unique alleles ([Obs_Total_alleles_grouped.csv](Obs_Total_alleles_grouped.csv)).

So far, the data suggest the presence of a high number of novel alleles, that is alleles with no reference in the IMGT/HLA database ([novel_alleles.csv](novel_alleles.csv)). Six of which are found in the Class II HLA loci. The DPA1 loci has the highest number with 3 novel alleles. A novel allele of particular interest is the presence of a nonsynonymous mutation in the start codon of the promoter region of the DPA1 loci (DPA1*03:01@2). This mutation changes the nucleotide codon sequence from ATG to ACG, corresponding to an amino-acid altering substitution in the start codon of the exon, from Methionine to Threonine This amino-acid altering mutation may be implicated in changes in the protein expression with possible functional implications. 

At this time, it is unknown whether the high density of novel alleles observed is due to the low representation of the East African population in the International ImMunoGeneTics Information System (IMGT)/HLA Database or it is related to a unique phenotype presented by hemorrhagic fever survivors.   Interest of our lab and collaborators includes the development of associational studies to determine whether disease outcomes are related to specific HLA types.

A comprehensive list of the 138 HLA alleles sequenced and their frequencies in the EBOV and LASV groups is presented in ([list_of_alleles.csv](list_of_alleles.csv)). 

Thus far, the results of this project have contributed in the efforts to characterize the under-represented West African population in the IMGT/HLA database, and most importantly, these results may shed light in understanding the contribution of specific HLA genotypes in association with outcomes of hemorrhagic fever infection in the West African population. 

### Allele Frequencies in EVD vs LASV patients.

![Allele Frequency](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/allele_frequency.png)
