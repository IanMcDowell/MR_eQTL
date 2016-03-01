#!/tigress/BEE/tools/anaconda/bin/python
import numpy as np
from sys import argv
import json

observed_t_MRs = argv[1]
permuted_t_MRs = argv[2]
fdrs_out = argv[3]

# observed_t_MRs = "t_MRs.pc_to_pc.observed.npy"
# permuted_t_MRs = "t_MRs.pc_to_pc.permuted.npy"
# fdrs_out = "t_MRs.pc_to_pc.fdrs.json"

observed_t_MRs = np.load(observed_t_MRs)
permuted_t_MRs = np.load(permuted_t_MRs)

observed_t_MRs = observed_t_MRs[observed_t_MRs < np.inf]
permuted_t_MRs = permuted_t_MRs[permuted_t_MRs < np.inf]

def create_fdrs_list(observed, permuted):
    fdrs = []
    for i, val in enumerate(np.linspace(start=0, stop=observed.max(), num=1000)):
        sig_null = len(permuted[permuted >= val])
        sig_real = len(observed[observed >= val])
        try:
            print 'FDR', str(val), str(sig_null), str(sig_real), str(float(sig_null)/float(sig_real))
        except ZeroDivisionError:
            print 'FDR', str(val), str(sig_null), str(sig_real), 0.0
        
        fdrs.append((sig_null, sig_real, val))
        # track progress
        if i % 1000 == 0:
            print '%0.1f%% complete'%(i / 10.0)
        
    return(fdrs)

fdrs = create_fdrs_list(observed_t_MRs, permuted_t_MRs)

with open(fdrs_out, 'w') as f:
    json.dump(fdrs, f)
