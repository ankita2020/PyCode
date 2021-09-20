#Enter the column which has string data type
column=''
import _helper
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import json

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    tfidf = TfidfVectorizer()
    if column in df:
        tf_idf_data = tfidf.fit_transform(df[column])
        tfidf_list = tf_idf_data.toarray()
        df_tfidf = pd.DataFrame(tfidf_list)
        
    else:
        return None
    
    return _helper.publish(df_tfidf)
  
