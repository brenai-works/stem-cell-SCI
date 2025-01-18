# core
import numpy as np
import pandas as pd

def calculate_percentage_agreement(prt, _dataset, _ref_set):
    print(">> calculate percentage agreement across all agents [...]")
    agreement_tab = pd.DataFrame({"id":[], "title":[], "agreement":[]})
    # cross-ref titles in the reference set with human and llm responses in dataset (using id and list key)
    df = pd.DataFrame(_dataset)
    idx_lst = df.index.tolist()
    n_raters = int(_dataset.shape[_dataset.ndim - 1])
    paper_id = []
    paper_title = []
    paper_agreed = []
    raters = []
    for idx in idx_lst:
        for r_idx in range(len(_ref_set)):
            if int(idx) == int(_ref_set.iloc[r_idx]["id"]):
                # for each paper/record calculate the % agreement across multiple human and llm agents
                paper_id.append(int(idx))
                paper_title.append(_ref_set.iloc[r_idx]["title"])
                df_results = pd.crosstab(list(df.iloc[idx]), columns=[True, False], normalize="all", dropna=False)
                row = len(df_results)
                if row > 1:
                    n_tp = float(df_results.iloc[1][1])        # true positive
                    n_tn = float(df_results.iloc[0][0])        # true negative
                    n_fn = float(df_results.iloc[0][1])        # false negative
                    n_fp = float(df_results.iloc[1][0])        # false positive
                else:
                    row1 = bool(df_results.index[0])
                    if row1:
                        n_tp = float(df_results.iloc[0][1])    # true positive
                        n_tn = float(0.0)                      # true negative
                        n_fn = float(df_results.iloc[0][0])    # false negative
                        n_fp = float(0.0)                      # false positive 
                    else:
                        n_fp = float(df_results.iloc[0][0])    # false positive
                        n_tp = float(0.0)                      # true positive
                        n_tn = float(df_results.iloc[0][1])    # true negative
                        n_fn = float(0.0)                      # false negative
                if n_tn == n_tp:
                    if n_tn > float(0.0) or n_tp > float(0.0):                      # want to check if true positive and negative values
                        percentage_agreeement = float(0.0)
                    else:
                        percentage_agreeement = n_tn + n_tp
                elif n_tn > n_tp:
                    if n_fp > float(0.0) or n_fn > float(0.0) or n_tp > float(0.0): # want to check for false negatives and positive values
                        percentage_agreeement = n_tn + n_fp
                    else:
                        percentage_agreeement = float(0.0)
                elif n_tn < n_tp:
                    if n_fn > float(0.0) or n_fp > float(0.0) or n_tp > float(0.0): # want to check for false negatives and positives values
                        percentage_agreeement = n_tp + n_fn
                    else:
                        percentage_agreeement = float(0.0) 
                paper_agreed.append(percentage_agreeement)
                rater = []
                for rater_idx in range(0, n_raters):
                    rater.append(df.iloc[idx][rater_idx])
                raters.append(rater)
    agreement_tab["id"] = paper_id
    agreement_tab["title"] = paper_title
    agreement_tab["agreement"] = paper_agreed
    agreement_tab["scores"] = raters 
    # calculate overall interrater reliability
    overall_interrater_reliability = agreement_tab["agreement"].sum()/len(_dataset)
    if prt:
        print("")
        print(agreement_tab)
        print("")
        print("Overall Agreement: " + str(overall_interrater_reliability))
        print("")
    return agreement_tab

def show_low_aggreement_papers_with(threshold, dataset, ref_set):
    low_agreement_papers = pd.DataFrame({})
    agreement_tab = calculate_percentage_agreement(prt=True, _dataset=dataset, _ref_set=ref_set)
    print(">> showing papers with low aggreement scores [...]")
    # retrieve papers/records that fall below threshold

    # identify any raters (human and llm agent) outliers

    return low_agreement_papers