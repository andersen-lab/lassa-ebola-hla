*Summary: HLA genotyping of Lassa and Ebola patients. [Data here](https://github.com/andersen-lab/lassa-ebola-hla).*

In an effort to increase our understanding of the immune response to Lassa virus (LASV) and Ebola virus (EBOV), we are typing the human leukocyte antigen (HLA) genes from Lassa and Ebola patients, as well as healthy individuals.

We perform the HLA typing using the Illumina TruSight HLA Sequencing Panel, which allows for the isolation and amplification of 11 HLA loci (Class I HLA-A, -B, -C; Class II HLA-DRB1/3/4/5, -DQA1, -DQB1, -DPA1, -DPB1) using long range PCR. Amplicons are used to produce libraries using the Illumina Nextera protocol and sequenced on the Illumina MiSeq platform. HLA-optimized software is used to analyze sequence data, produce consensus sequences and compare them to to the IMGT/HLA database for HLA genotype assignments.

To date, we have sequenced and genotyped 39 PBMC samples from Lassa and Ebola patients (22 Ebola + 17 Lassa), resulting in a total of 702 alleles sequenced ([Obs_Total_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles.csv)). Ebola patients yielded 109 unique alleles and Lassa patients yielded 108 unique alleles ([Obs_Total_alleles_grouped.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/Obs_Total_alleles_grouped.csv)). As part of a collaboration with the Broad Institute, we also have HLA types from another hundred Sierra Leonean individuals. Together with Illumina, we are planning to type another couple of hundred individuals by the end of 2017 and will release the data here once generated - stay tuned.

So far, the data suggest the presence of a high number of novel alleles - that is alleles with no reference in the IMGT/HLA database ([novel_alleles.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/novel_alleles.csv)). Six of these are found in the Class II HLA loci. The DPA1 loci has the highest number with 3 novel alleles. A novel allele of particular interest is the presence of a nonsynonymous mutation in the start codon (ATG to ACG) of the DPA1 loci (DPA1*03:01@2). 

A comprehensive list of the 138 HLA alleles sequenced and their frequencies is presented in ([allele_frequencies.csv](https://github.com/andersen-lab/lassa-ebola-hla/blob/master/allele_frequencies.csv))). 

Thus far, the results of this project have contributed in the efforts to characterize the under-represented West African population in the IMGT/HLA database, and most importantly, these results may shed light in understanding the contribution of specific HLA genotypes in association with outcomes of hemorrhagic fever infection in the West African population. 

### Allelic Frequencies(>5%).

#### MHC-I
| Gene | Allele | Allelic Frequency(> 5%) |
| --- | --- | --- |
|HLA-A|A*020101|0.115384615385|
|HLA-A|A*030101|0.115384615385|
|HLA-A|A*300201|0.115384615385|
|HLA-A|A*300101|0.115384615385|
|HLA-A|A*740101|0.102564102564|
|HLA-A|A*230101|0.0769230769231|
|HLA-A|A*680101|0.0641025641026|
|HLA-A|A*330301|0.0641025641026|
|HLA-A|A*290201|0.0512820512821|
|HLA-A|A*800101|0.025641025641|
|HLA-A|A*660101|0.025641025641|
|HLA-A|A*3601|0.025641025641|
|HLA-A|A*340201|0.025641025641|
|HLA-A|A*330101|0.0128205128205|
|HLA-A|A*320101|0.0128205128205|
|HLA-A|A*240201|0.0128205128205|
|HLA-A|A*2317|0.0128205128205|
|HLA-A|A*010101|0.0128205128205|
|HLA-A|A*680201|0.0128205128205|
|HLA-B|B*530101|0.141025641026|
|HLA-B|B*420101|0.115384615385|
|HLA-B|B*350101|0.102564102564|
|HLA-B|B*580101|0.0769230769231|
|HLA-B|B*070201|0.0641025641026|
|HLA-B|B*150301|0.0641025641026|
|HLA-B|B*180101|0.0512820512821|
|HLA-B|B*440301|0.0384615384615|
|HLA-B|B*570201|0.0384615384615|
|HLA-B|B*140201|0.025641025641|
|HLA-B|B*8201|0.025641025641|
|HLA-B|B*35@1|0.025641025641|
|HLA-B|B*820201|0.025641025641|
|HLA-B|B*450101|0.025641025641|
|HLA-B|B*151601|0.025641025641|
|HLA-B|B*080101|0.025641025641|
|HLA-B|B*8101|0.0128205128205|
|HLA-B|B*520102|0.0128205128205|
|HLA-B|B*570301|0.0128205128205|
|HLA-B|B*070601|0.0128205128205|
|HLA-B|B*151801|0.0128205128205|
|HLA-B|B*151001|0.0128205128205|
|HLA-B|B*2703|0.0128205128205|
|HLA-B|B*560101|0.0128205128205|
|HLA-B|B*270502|0.0128205128205|
|HLA-B|B*780101|0.0128205128205|
|HLA-C|C*040101|0.166666666667|
|HLA-C|C*030202|0.128205128205|
|HLA-C|C*170101|0.128205128205|
|HLA-C|C*021001|0.0897435897436|
|HLA-C|C*160101|0.0769230769231|
|HLA-C|C*0718|0.0641025641026|
|HLA-C|C*070201|0.0512820512821|
|HLA-C|C*1802|0.0512820512821|
|HLA-C|C*150502|0.0384615384615|
|HLA-C|C*030301|0.025641025641|
|HLA-C|C*060201|0.025641025641|
|HLA-C|C*050101|0.025641025641|
|HLA-C|C*140201|0.025641025641|
|HLA-C|C*1801|0.0128205128205|
|HLA-C|C*030402|0.0128205128205|
|HLA-C|C*080206|0.0128205128205|
|HLA-C|C*080201|0.0128205128205|
|HLA-C|C*010201|0.0128205128205|
|HLA-C|C*1601@8|0.0128205128205|
|HLA-C|C*070101|0.0128205128205|
|HLA-C|C*020202|0.0128205128205|

#### MHC-II
| Gene | Allele | Allelic Frequency(> 5%) |
| --- | --- | --- |
|HLA-DPA1|DPA1*020101|0.307692307692|
|HLA-DPA1|DPA1*020108|0.192307692308|
|HLA-DPA1|DPA1*020202|0.128205128205|
|HLA-DPA1|DPA1*0301|0.102564102564|
|HLA-DPA1|DPA1*0301@2|0.0897435897436|
|HLA-DPA1|DPA1*010301|0.0641025641026|
|HLA-DPA1|DPA1*0207@4|0.0641025641026|
|HLA-DPA1|DPA1*0301@3|0.0512820512821|
|HLA-DPB1|DPB1*010101|0.333333333333|
|HLA-DPB1|DPB1*10501|0.153846153846|
|HLA-DPB1|DPB1*010102|0.102564102564|
|HLA-DPB1|DPB1*1701|0.0897435897436|
|HLA-DPB1|DPB1*8501|0.0641025641026|
|HLA-DPB1|DPB1*4001|0.0641025641026|
|HLA-DPB1|DPB1*130101|0.0512820512821|
|HLA-DPB1|DPB1*110101|0.025641025641|
|HLA-DPB1|DPB1*030101|0.025641025641|
|HLA-DPB1|DPB1*13101|0.025641025641|
|HLA-DPB1|DPB1*040201|0.025641025641|
|HLA-DPB1|DPB1*040101|0.0128205128205|
|HLA-DPB1|DPB1*020102|0.0128205128205|
|HLA-DPB1|DPB1*390101|0.0128205128205|
|HLA-DQA1|DQA1*050501|0.230769230769|
|HLA-DQA1|DQA1*010201|0.217948717949|
|HLA-DQA1|DQA1*040101|0.192307692308|
|HLA-DQA1|DQA1*030301|0.141025641026|
|HLA-DQA1|DQA1*010202|0.0641025641026|
|HLA-DQA1|DQA1*040102|0.0641025641026|
|HLA-DQA1|DQA1*020101|0.0512820512821|
|HLA-DQA1|DQA1*010102|0.025641025641|
|HLA-DQA1|DQA1*010301|0.0128205128205|
|HLA-DQB1|DQB1*031901|0.205128205128|
|HLA-DQB1|DQB1*040201|0.179487179487|
|HLA-DQB1|DQB1*020201|0.141025641026|
|HLA-DQB1|DQB1*060901|0.102564102564|
|HLA-DQB1|DQB1*050101|0.0641025641026|
|HLA-DQB1|DQB1*030101|0.0641025641026|
|HLA-DQB1|DQB1*050201|0.0512820512821|
|HLA-DQB1|DQB1*030201|0.0512820512821|
|HLA-DQB1|DQB1*060201|0.0512820512821|
|HLA-DQB1|DQB1*0309|0.0128205128205|
|HLA-DQB1|DQB1*060401|0.0128205128205|
|HLA-DQB1|DQB1*060501|0.0128205128205|
|HLA-DQB1|DQB1*0502@6|0.0128205128205|
|HLA-DQB1|DQB1*04@5|0.0128205128205|
|HLA-DQB1|DQB1*060301|0.0128205128205|
|HLA-DQB1|DQB1*030104|0.0128205128205|
|HLA-DRB1|DRB1*030201|0.192307692308|
|HLA-DRB1|DRB1*130201|0.153846153846|
|HLA-DRB1|DRB1*080401|0.0769230769231|
|HLA-DRB1|DRB1*110201|0.0641025641026|
|HLA-DRB1|DRB1*090102|0.0641025641026|
|HLA-DRB1|DRB1*110102|0.0641025641026|
|HLA-DRB1|DRB1*160201|0.0512820512821|
|HLA-DRB1|DRB1*070101|0.0512820512821|
|HLA-DRB1|DRB1*040501|0.0512820512821|
|HLA-DRB1|DRB1*120101|0.0384615384615|
|HLA-DRB1|DRB1*130301|0.0384615384615|
|HLA-DRB1|DRB1*1304|0.0384615384615|
|HLA-DRB1|DRB1*110101|0.025641025641|
|HLA-DRB1|DRB1*130101|0.025641025641|
|HLA-DRB1|DRB1*010201|0.025641025641|
|HLA-DRB1|DRB1*0806|0.0128205128205|
|HLA-DRB1|DRB1*040101|0.0128205128205|
|HLA-DRB1|DRB1*150301|0.0128205128205|
|HLA-DRB3|DRB3*010102|0.406779661017|
|HLA-DRB3|DRB3*020201|0.305084745763|
|HLA-DRB3|DRB3*030101|0.28813559322|
|HLA-DRB4|DRB4*010301|0.571428571429|
|HLA-DRB4|DRB4*010101|0.428571428571|
|HLA-DRB5|DRB5*02@7|0.8|
|HLA-DRB5|DRB5*010101|0.2|

#### Allele Frequencies in EVD vs LASV patients.

\*Novel Alleles highlighted in <span style="color: red;">RED</span>.

![Allele Frequency](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/allelic_frequency.png)

![Counts per HLA Gene](https://raw.githubusercontent.com/andersen-lab/lassa-ebola-hla/master/img/counts.png)
