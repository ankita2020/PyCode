#Enter the column names in the list below
col=[]

import _helper
import pandas as pd
from numpy import log
from numpy import sqrt


def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    for c in col:
        if c in df:
            df[c + 'sqrt_col'] = sqrt(df[c])

        else:
            return None
    
    return _helper.publish(df)
