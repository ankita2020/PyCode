#Enter column names in the list defined below
columns=[]
# pass the float value in n variable for find n_root_mean value
m=
import _helper
import pandas as pd
import math
import json

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    for col in columns:
        if col in df.columns:
            df[col+"_n_root"]=df[col]**m
            

        else:
            return None
        
    return _helper.publish(df)


