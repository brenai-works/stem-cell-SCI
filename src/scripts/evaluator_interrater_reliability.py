# core
import numpy as np
import pandas as pd
import os
from pathlib import Path
import io
import sys, getopt
import json
import csv

# stats
from scipy import stats
from statsmodels.stats.inter_rater import cohens_kappa
from statsmodels.stats.inter_rater import to_table

# file path
from dir import human_agent_responses_file
from dir import pwd_human
from dir import llm_agent_responses_file
from dir import pwd_llm

# main
def main(argv):
    # command line UI 
    opts, args = getopt.getopt(argv, "-ha:s:", ["llmAgent_responses=", "show_low_agreement="])
    llmAgent_responses_file = ""
    show_low_aggree = ""

    for opt, arg in opts:
        if opt == '-h':
            print("")
            print("evaluator_interrater_reliability.py \n -a <LLM agent responses> \n -s <show low aggreement papers (y|n)>")
            print("")
            sys.exit()
        elif opt in ("-a", "--llmAgent_responses"):
            llmAgent_responses_file = arg
        elif opt in ("-s", "--show_low_agreement"):
            show_low_aggree = arg

    if llmAgent_responses_file == "":
        print("")
        print('Error: Endpoint require value for -a or --llmAgent_responses.')
        print("")
        sys.exit()

    if show_low_aggree != "":
        if show_low_aggree.lower() != "y" and show_low_aggree.lower() != "n":
            print("")
            print('Error: Endpoint require value Y for yes or N for no for -s or --show_low_agreement.')
            print("")
            sys.exit() 

    print("")
    print("Evaluator Interrater Reliability version 0.1 (11 Jan 2024)")
    print("Endpoint: Evaluate LLM Response against Human Response")
    print("")
    print("LLM Responses in valid JSON file:")
    print(llmAgent_responses_file)
    print("")
    if show_low_aggree != "":
        print("Show low aggreeement papers:")
        print(show_low_aggree)
        print("")

    # read the human rater responses
    df_human = read_human_rater_responses(prt=True)

    # read the llm rater responses and transform into dataframe
    df_llm = read_llm_rater_responses(prt=True)

    # calculate the aggreement levels for each human and llm responses (matched by paper title)

    # calculate Kappa's statistic 

    # calculate Confidence Intervals (CI)

    # show records/papers to human agents for further group discussion
    if show_low_aggree.lower() == "y": 
        show_low_aggreement_papers_with(scores_under=0.60)
        print("")
        sys.exit() 
    elif show_low_aggree.lower() == "n" or show_low_aggree.lower() == "":
        print("")
        sys.exit() 
    else:
        print("")
        print("Error: Invalid option for showing low agreement papers, must be (y|n).")
        print("")
        sys.exit() 

def read_human_rater_responses(prt):
    pwd = str(Path.home()) + pwd_human
    with open(os.path.join(pwd, human_agent_responses_file), 'r') as fp:
        df = pd.read_csv(fp)
        human_rater_resp = pd.DataFrame.from_dict({"title":df["Title"], 
                                                   "authors":df["Authors"], 
                                                   "included":np.array(df["Included"], dtype=bool), 
                                                   "excluded":np.array(df["Excluded"], dtype=bool)}) # may include reason for exclusion later    
    print(">> read human responses [...]")
    if prt:
        print(human_rater_resp)
    return human_rater_resp

def read_llm_rater_responses(prt):
    pwd = str(Path.home()) + pwd_llm
    _title = []
    _authors = []
    _included = []
    _excluded = []
    _reason = []
    with open(os.path.join(pwd, llm_agent_responses_file), 'r') as fp:
        json_doc = json.load(fp)
        for df in json_doc:
            _title.append(df["title"])
            _authors.append(df["authors"])
            _included.append(eval(str(df["inclusion"])))
            _excluded.append(eval(str(df["exclusion"])))
            _reason.append(df["reason for exclusion"])
        llm_rater_resp = pd.DataFrame.from_dict({"title":_title,
                                                "authors":_authors,
                                                "included":_included,
                                                "excluded":_excluded,
                                                "reason":_reason})
    print(">> read llm responses [...]")
    if prt:
        print(llm_rater_resp)
    return llm_rater_resp

def prepare_dataset(_human, _llm):
    print(">> prepare dataset for analysis [...]")

def show_low_aggreement_papers_with(scores_under):
    print(">> showing papers with low aggreement scores [...]")

if __name__ == "__main__":
   main(sys.argv[1:])