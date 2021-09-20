#Enter the positive or negative or both in var
var=''
import _helper
import pandas as pd
import math
import numpy as np
import json


def main():
    data = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    if var == 'positive':
        data['positive_count'] = data.select_dtypes(include='number').ge(1).sum(axis=1)
        
    elif var == 'negative':
        data['negative_count'] = data.select_dtypes(include='number').lt(0).sum(axis=1)
        
    elif var == 'both':
        data['positive_count'] = data.select_dtypes(include='number').ge(1).sum(axis=1)
        data['positive_count'] = data.select_dtypes(include='number').lt(0).sum(axis=1)
  
    else:
        return None
    
    return _helper.publish(data)
