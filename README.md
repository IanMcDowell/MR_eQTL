
# Trans-eQTL Mendelian Randomization

## Purpose

This package includes scripts that may be used to test for gene-gene trans associations using genotype and gene expression data. Briefly, genotypes (z) are tested for association with genes in cis (x) and for association with genes in trans (y). A statistic based on the ratio of the trans effect size to the cis effect size can be used to quantify the association between gene x and gene y. Here, scripts are provided for the computation of the estimated trans effect size of gene x on gene y and the standard error of that estimate. The ratio of the squared trans effect size to the standard error yields a test statistic that is roughly chi-squared distributed, much like a Wald test (see equations below). A script is provided to compute the false discovery rate if test statistics are computed for both observed data and permuted data (where subject labels of expression matrix Y are shuffled).

![MR diagram](https://github.com/IanMcDowell/MR_eQTL/blob/master/auxiliary/PMID17886233_fig1.png)
    
For more details, see e.g. [PMID: 17886233](http://www.ncbi.nlm.nih.gov/pubmed/17886233)

## Installation and Prerequisites

It is assumed that the user will have the following python packages installed:
  * numpy
  * pandas

Installation proceeds as follows:

python setup.py install 


## Usage

It is required that the user of this package has the following data:
  * expression dataframe of genes with cis-eQTL associations, `X.txt`
  * expression dataframe of genes tested for trans-eQTL associations, `Y.txt`
  * permuted expression dataframe of genes tested for trans-eQTL associations, `Y.permuted.txt`
  * genotypes dataframe, `Z.txt`
  * cis-eQTL association results, `z_to_x_top_beta.txt`
  * trans-eQTL association results, `trans.association.txt`
  * permuted trans-eQTL association results `trans.permuted.association.txt`
  
For details on the format of the above inputs, see help message of compute_t_MR.py.

Example usage:

```

cd MR_eQTL/test

compute_unscaled_var_beta_MR.py \
X.txt Z.txt unscaled_var_beta_MR.npy

compute_t_MR.py \
-i trans.association.txt \
-X X.txt \
-Y Y.txt \
-Z Z.txt \
-b z_to_x_top_beta.txt \
-v unscaled_var_beta_MR.npy \
-t t_MRs.npy \
-o MR_association_results.txt

compute_t_MR.py \
-i trans.permuted.association.txt \
-X X.txt \
-Y Y.permuted.txt \
-Z Z.txt \
-b z_to_x_top_beta.txt \
-v unscaled_var_beta_MR.npy \
-t t_MRs.permuted.npy \
-o MR_association_results.permuted.txt

compute_FDR_t_MR.py \
t_MRs.npy t_MRs.permuted.npy fdrs.json

CUTOFF_FDR_05=$(find_test_statistic_cutoff_given_fdr.py fdrs.json 0.05)
awk -v cutoff=$CUTOFF_FDR_05 '$3 >= cutoff {print $0}' MR_association_results.txt \
> MR_association_results.sig_FDR_0.05.txt 

```

## License

TBD