# enter the column name which has integer or float datatype
column_1=''
column_2=''
#Enter the exponent values for the two columns
m =
n =
import _helper
import pandas as pd
import math
import json

def main():
    data = _helper.data() 
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    if column_1 in data.columns and column_2 in data.columns :
        data['exp'] = pow(data[column_1],m) - pow(data[column_2],n)
        
    else:
        return None
    
    return _helper.publish(data)

    
