#Enter column names in the list defined below
columns = []

#window size is the number of observations used for calculating the statistic.
win_size=

win_size_type = ''
#window_by_row - Window size by number of rows (For eq - 1,2,3,4,5...)
#window_by_time- Window size by datetime (For eq - '1D','1H','1min','1s'....)

method_type=''
#Provide a method type like expanding or rolling
#If method_type is expanding so it only works on window_by_row and window_type should be a comment.

#Provide a operation like sum or mean or median or count or variance or quantile.
operation=''

percentile=
#provide a first quantile 0-0.25 or second quantile 0.25-0.50 or third quantile 0.50-0.75 or 4th quantile 0.75-1.00
# percentile only to be used when window_by_column selected as in window_size_type and 'quantile' selected in operation 

import _helper
import pandas as pd
import numpy as np
import re
import pandas
import json
import random
from datetime import datetime, timedelta

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    for col in columns :
        if method_type=='rolling':
            if win_size_type=='window_by_row':
                if operation =="sum":
                    df[col+"_sum"] = df[col].rolling(win_size).sum()

                elif operation =="mean":
                    df[col+"_mean"] = df[col].rolling(win_size).mean()

                elif operation =="median":
                    df[col + "_median"] = df[col].rolling(win_size).median()

                elif operation =="count":
                    df[col + "_count"] = df[col].rolling(win_size).count()

                elif operation =="quantile":
                    df[col + "_quantile"] = df[col].rolling(win_size).quantile(percentile)

                else:
                    df[col + "_variance"] = df[col].rolling(win_size).var()


            elif win_size_type=='window_by_time':

                if type(df.index) == pandas.core.indexes.datetimes.DatetimeIndex :

                    if operation =="sum":
                        df[col + "_sum"] = df[col].rolling(win_size).sum()

                    elif operation =="mean":
                        df[col + "_mean"] = df[col].rolling(win_size).mean()

                    elif operation =="median":
                        df[col + "_median"] = df[col].rolling(win_size).median()

                    elif operation =="count":
                        df[col + "_count"] = df[col].rolling(win_size).count()

                    elif operation =="quantile":
                        df[col + "_quantile"] = df[col].rolling(win_size).quantile(percentile)

                    else:
                        df[col + "_variance"] = df[col].rolling(win_size).var()

                else:
                    min_year=1900
                    max_year=datetime.now().year

                    start = datetime(min_year, 1, 1, 00, 00, 00)
                    years = max_year - min_year+1
                    end = start + timedelta(days=365 * years)

                    for i in range(len(df)):
                        random_date = start + (end - start) * random.random()
                        df["date"] = random_date

                    df = df.set_index(df['date'])

                    if operation =="sum":
                        df[col + "_sum"] = df[col].rolling(win_size).sum()

                    elif operation =="mean":
                        df[col + "_mean"] = df[col].rolling(win_size).mean()

                    elif operation =="median":
                        df[col + "_median"] = df[col].rolling(win_size).median()

                    elif operation =="count":
                        df[col + "_count"] = df[col].rolling(win_size).count()

                    elif operation =="quantile":
                        df[col + "_quantile"] = df[col].rolling(win_size).quantile(percentile)

                    else:
                        df[col + "_variance"] = df[col].rolling(win_size).var()

            else:
                pass
        else:
            if operation =="sum":
                df[col+"_sum"] = df[col].expanding(win_size).sum()

            elif operation =="mean":
                df[col+"_mean"] = df[col].expanding(win_size).mean()

            elif operation =="median":
                df[col + "_median"] = df[col].expanding(win_size).median()

            elif operation =="count":
                df[col + "_count"] = df[col].expanding(win_size).count()

            elif operation =="quantile":
                df[col + "_quantile"] = df[col].expanding(win_size).quantile(percentile)

            else:
                df[col + "_variance"] = df[col].expanding(win_size).var()

            

    return _helper.publish(df)
