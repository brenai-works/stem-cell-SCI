# core
import numpy as np
import pandas as pd
from tabulate import tabulate

# stats
from statsmodels.stats.inter_rater import cohens_kappa
from statsmodels.stats.inter_rater import to_table

def calculate_agreement_level(prt, dataset):
    print(">> calculate agreement levels on entire dataset [...]")
    arr = to_table(data=dataset, bins=None)
    data = {
        "values":[arr[0][0][0], arr[0][0][1], arr[0][1][0], arr[0][1][1]],
        "llm agent":["Not Include"] * 2 + ["Include"] * 2,
        "human agent":["Not Include", "Include"] * 2
    }
    df = pd.DataFrame(data)
    tab = pd.pivot(df, values="values", index="llm agent", columns="human agent")
    if prt:
        print("")
        print("# of papers: " + str(len(dataset)))
        print("")
        print(tabulate(tab, headers=["Human agent\nLLM agent", "Include", "Not Include"], tablefmt="psql"))
        print("")
        print("CI Low: " + str(arr[1:2][0][0]))
        print("CI High: " + str(arr[1:2][0][2]))
        print("P-Value: " + str(arr[1:2][0][1]))
        print("-----")
    return arr

def calculate_kappa_statistics(prt, cont_tab):
    print(">> calculate Kappa's statistics [...]")
    tab = np.array([cont_tab[0][0], cont_tab[0][1]])
    results = cohens_kappa(table=tab, weights=None, return_results=True, wt=None)
    if prt:
        print("")
        print(results)
        print("")
    return results