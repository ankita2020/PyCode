#Enter column names in the list defined below
columns=[]
# pass the integer value in n variable for find square
n=
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
            df[col+"_n_power"]=df[col]**n
            
        else:
            return None
        
    return _helper.publish(df)
