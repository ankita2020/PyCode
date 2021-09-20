#Enter the column name in a list columns
columns=[]
#Enter 'add' or'sub'or'mul' or 'div' in oper
oper=''
import _helper
import pandas as pd
import json

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    for col in columns[0:1]:
        if oper =='add':
            df['add'] = df[col]
        elif oper =='sub':
            df['sub'] = df[col]
        elif oper =='mul':
            df['mul'] = df[col]
        elif oper =='div':
            df['div'] = df[col]
        else:
            return None
        
        for col in columns[1:]:
            if oper =='add':
                df['add'] += df[col]
                
            elif oper =='sub':
                df['sub'] -= df[col]
                
            elif oper =='mul':
                df['mul'] *= df[col]
                
            elif oper =='div':
                df['div'] /= df[col]
                
            else:
                return None
            
    return _helper.publish(df)
         
