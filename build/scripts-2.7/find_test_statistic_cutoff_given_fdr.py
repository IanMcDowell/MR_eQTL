#!/tigress/BEE/tools/anaconda/bin/python
import json
from sys import argv

fdrs = argv[1]
fdr = float(argv[2])

with open(fdrs, 'r') as f:
    fdrs = json.load(f)

def find_stat_cutoff_given_fdr(fdrs, cutoff):
    for (sig_null, sig_real, val) in fdrs:
        fdr = sig_null/float(sig_real) if sig_real != 0 else 1.0
        if fdr < cutoff:
            return val
    return None

stat_cutoff = find_stat_cutoff_given_fdr(fdrs, fdr)
print stat_cutoff