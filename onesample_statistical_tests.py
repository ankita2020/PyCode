# one sample t-test
#Enter column name having numerical values
col=''
t_test=''
import numpy as np
import _helper
from scipy.stats import ttest_1samp, wilcoxon, shapiro

def main():
    df= _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    if t_test=='student t_test':
        # null hypothesis: expected value =
        t_statistic, p_value = ttest_1samp(df[col], 0)
    elif t_test=='sign_test':
        # one sample wilcoxon-test
        z_statistic, p_value = wilcoxon(df[col])
    else:
        #on esample shapiro
        stat, p_value = shapiro(df[col])
        p_value = "{:.5f}".format(p_value)
    df[col +"_p_value"]=p_value
    return _helper.publish(df)
