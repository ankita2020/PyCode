#Enter columns name  in col which have numerical values
col=[]

from gauss_rank_scaler.gauss_rank_scaler import GaussRankScaler
import _helper
import pandas as pd

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    for c in col:
        if c in df:
            scaler = GaussRankScaler()
            X = scaler.fit_transform(df[[c]])
            X_ = pd.DataFrame(X, columns=[c +'_gauss_rank'])
            df=df.join(X_)

        else:
            return None
    
    return _helper.publish(df)
