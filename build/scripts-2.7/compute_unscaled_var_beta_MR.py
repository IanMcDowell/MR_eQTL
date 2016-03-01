#!/tigress/BEE/tools/anaconda/bin/python
import pandas as pd
import json
import numpy as np
from sys import argv

X = argv[1]
Z = argv[2]
unscaled_var_beta_MR_out = argv[3]

# X is a dataframe with header of samples (e.g. individuals) and with row indices
# for the name of each element of the independent variable X (e.g. gene names)
# and thus is of dimension: number of tested independent variables + 1 by number of samples + 1

# Z is a dataframe with header of samples (e.g. individuals) and with row indices
# for the name of each element of the instrumental variable Z (e.g. SNP rsIDs)
# and thus is of dimension: number of tested instrumental variables + 1 by number of samples + 1

X = pd.read_csv(X, index_col=0, sep='\t')
Z = pd.read_csv(Z, index_col=0, sep='\t')

assert(X.shape[1] == Z.shape[1])
assert(list(X.columns) == list(Z.columns))

X = np.array(X)
Z = np.array(Z)

inner = np.diag(np.diag(np.inner(Z,Z))) 
inner_inv = np.linalg.inv(inner)
unscaled_var_beta_MR = np.dot(np.dot(X,Z.T)**2, inner_inv).T

np.save(unscaled_var_beta_MR_out, unscaled_var_beta_MR)
