
import _helper
import pandas as pd
import numpy as np
import plotly as py
import plotly.express as px

col1 = ''
col2 = ''
color_col = ''

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    fig = px.histogram(df, x=col1, y=col2, color=color_col, marginal="box",hover_data=df.columns)
    _helper.chart(fig)
    

