# core
import numpy as np
import pandas as pd
import os
from pathlib import Path
import json

# file path
from dir import human_agent_responses_file
from dir import pwd_human
from dir import llm_agent_responses_file
from dir import pwd_llm

def read_human_rater_responses(prt):
    print(">> read human responses [...]")
    pwd = str(Path.home()) + pwd_human
    with open(os.path.join(pwd, human_agent_responses_file), 'r') as fp:
        df = pd.read_csv(fp)
        human_rater_resp = pd.DataFrame.from_dict({"title":df["Title"], 
                                                   "authors":df["Authors"], 
                                                   "included":np.array(df["Included"], dtype=bool), 
                                                   "excluded":np.array(df["Excluded"], dtype=bool)}) # may include reason for exclusion later    
    if prt:
        print(human_rater_resp)
    return human_rater_resp

def read_llm_rater_responses(prt):
    print(">> read llm responses [...]")
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
    if prt:
        print(llm_rater_resp)
    return llm_rater_resp