# core
import numpy as np
import pandas as pd
import os
import io
import sys, getopt
import json

# stats
from scipy import stats
from statsmodels.stats.inter_rater import cohens_kappa
from statsmodels.stats.inter_rater import to_table

# main
def main(argv):
    # command line UI 
    opts, args = getopt.getopt(argv, "-ha:s:", ["llmAgent_responses=", "show_low_agreement="])
    human_agent_responses_file = "human_rater_title_abstract_author.csv"
    llmAgent_responses_file = ""
    show_low_aggree = ""

    for opt, arg in opts:
        if opt == '-h':
            print("")
            print("evaluator_interrater_reliability.py -a <LLM agent responses> -s <show low aggreement papers (y|n)>")
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

if __name__ == "__main__":
   main(sys.argv[1:])