import _helper
from scipy import stats
import pandas as pd
import json

def main():
    df = _helper.data()
    #Enter the column which has integer data type
    col=''
    if col in df:
        if df[col].dtypes=='float64':
            df[col]=df[col].astype(int)
            transform = df[col].values
            # transform values and store as "dft"
            dft = stats.boxcox(transform)
            df['box_cox'] = dft[0]
            return _helper.publish(df)
    else:
        return 'Column does not exist'

    return _helper.publish(df)
        
