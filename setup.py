from distutils.core import setup 

setup(name='MR_eQTL',
      version='1.0',
      description='Mendelian randomization for gene-gene association in trans.',
      author='Ian McDowell',
      author_email='ian.mcdowell@duke.edu',
      scripts=['bin/compute_unscaled_var_beta_MR.py',
               'bin/compute_t_MR.py', 
               'bin/compute_FDR_t_MR.py',
               'bin/find_test_statistic_cutoff_given_fdr.py']
     )