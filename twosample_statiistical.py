# Two sample t-test
#Enter column name having numerical values
#col_1 should be target variable and it should be a binary column
col_1=''
col_2=''

#enter t_test
t_test=''
import numpy as np
import pandas as pd
import _helper
from scipy.stats import ttest_ind,ks_2samp, median_test

def main():
    df=_helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    if t_test=='student t_test':
        # null hypothesis: expected value =
        a = df.loc[df[col_1] == df[col_1].value_counts().index[0], col_2].to_numpy()
        b = df.loc[df[col_1] == df[col_1].value_counts().index[1], col_2].to_numpy()
        t_statistic, p_value = ttest_ind(a,b)
    elif t_test=='Kolmogrov-Smirnov':
        # two sample Kolmogrov-Smirnov test t
        a = df.loc[df[col_1] == df[col_1].value_counts().index[0], col_2].to_numpy()
        b = df.loc[df[col_1] == df[col_1].value_counts().index[1], col_2].to_numpy()
        z_statistic, p_value = ks_2samp(a,b)
    else:
        #two sample median mood test
        a = df.loc[df[col_1] == df[col_1].value_counts().index[0], col_2].to_numpy()
        b = df.loc[df[col_1] == df[col_1].value_counts().index[1], col_2].to_numpy()
        stat, p_value,m,tb = median_test(a,b)
    p_value = "{:.30f}".format(p_value)
    df[col_1 +'_'+ col_2 + "_p_value"] = p_value
    
    return _helper.publish(df)
