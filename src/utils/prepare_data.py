# core
import numpy as np
import pandas as pd

def prepare_dataset_for_agreement(prt, _human, _llm):
    print(">> prepare dataset for analysis [...]")
    id = 0
    ref = pd.DataFrame.from_dict({"id":[], "title":[], "reason":[]})
    _id = []
    _titles = []
    _include = []
    _reasons = []
    val = []
    for i in range(len(_human)):
        for x in range(len(_llm)):
            if _human.iloc[i]["title"] == _llm.iloc[x]["title"] and _human.iloc[i]["authors"] == _llm.iloc[x]["authors"]:
                _id.append(id)
                _titles.append(_human.iloc[i]["title"])                
                _include.append(_human.iloc[i]["included"])
                _include.append(_llm.iloc[x]["included"])
                _reasons.append(_llm.iloc[x]["reason"])
                val.append(_include)
                _include = []
                id = id + 1
    ref["id"] = _id
    ref["title"] = _titles
    ref["reason"] = _reasons
    data = np.array(val)
    if prt:
        print(ref)
    return ref, data