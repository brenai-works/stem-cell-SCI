# core
import numpy as np
import pandas as pd

def prepare_dataset_for_aggreement(prt, _human, _llm):
    id = 0
    ref = pd.DataFrame.from_dict({"id":[], "title":[]})
    _id = []
    _titles = []
    _h_include = []
    _llm_include = []
    val = []
    for i in range(len(_human)):
        for x in range(len(_llm)):
            if _human.iloc[i]["title"] == _llm.iloc[x]["title"] and _human.iloc[i]["authors"] == _llm.iloc[x]["authors"]:
                _id.append(id)
                _titles.append(_human.iloc[i]["title"])                
                _h_include.append(_human.iloc[i]["included"])
                _llm_include.append(_llm.iloc[x]["included"])
                id = id + 1
    ref["id"] = _id
    ref["title"] = _titles
    val.append(_h_include)
    val.append(_llm_include)
    data = np.array(val)
    print(">> prepare dataset for analysis [...]")
    if prt:
        print(ref)
    return ref, data