# core
import numpy as np
import pandas as pd

# stats
from scipy import stats
from statsmodels.stats.inter_rater import cohens_kappa
from statsmodels.stats.inter_rater import to_table

def calculate_agreement_level(prt, dataset):
    print(">> calculate agreement levels on entire dataset [...]")