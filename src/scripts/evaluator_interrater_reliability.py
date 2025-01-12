# core
import numpy as np
import pandas as pd
import sys, getopt

# pipes
from src.pipes._get_responses import read_human_rater_responses
from src.pipes._get_responses import read_llm_rater_responses
from src.pipes.show_results import show_low_aggreement_papers_with

# utils
from src.utils.prepare_data import prepare_dataset_for_aggreement 
from src.utils.evaluate_data import calculate_agreement_level
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
        print("Show low aggreement papers:")
        print(show_low_aggree)
        print("")

    # read the human rater responses
    df_human = read_human_rater_responses(prt=False)

    # read the llm rater responses and transform into dataframe
    df_llm = read_llm_rater_responses(prt=False)

    # calculate the aggreement levels for each human and llm responses (matched by paper title & authors)
    reference, data = prepare_dataset_for_aggreement(prt=False, _human=df_human, _llm=df_llm)
    contigency_table = calculate_agreement_level(prt=True, dataset=data)

    # calculate Kappa's statistic 

    # calculate Confidence Intervals (CI)

    # show records/papers to human agents for further group discussion
    if show_low_aggree.lower() == "y": 
        show_low_aggreement_papers_with(scores_under=0.60, dataset=data)
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

if __name__ == "__main__":
   main(sys.argv[1:])