import _helper
import pandas as pd
import re
from pandas import read_csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
#Enter the column which has string data type
col=''

def main():
    df = _helper.data()
    if df.empty:
        raise ValueError('Data Loading failed !')
    else:
        pass
    #clean html
    def cleanhtml(sent):
        clean = re.sub(r'<*?>', r' ', str(sent))
        return clean

    #clean punctuation
    def cleanpunc(word):
        cleanr = re.sub(r'[?|!|\'|"|#]', r' ', str(word))
        cleaned = re.sub(r'[)|(|\|/]', r' ', str(cleanr))
        return cleaned

    lst_of_sent = []
    str1 = ''
    final_str = []
    #Enter the column which has string data type
    if col in df.columns:
        for sent in df[col].values:
            filtered_sent = []
            sent          = cleanhtml(sent)
            for word in sent.split():
                for clean_words in cleanpunc(word).split():
                    if (clean_words.isalpha()):
                        filtered_sent.append(clean_words.lower())
            lst_of_sent.append(filtered_sent)
    else:
        return None

    for lst in lst_of_sent:
        str1 = ' '.join(lst)
        final_str.append(str1)

    df[col] = final_str

    #Extract sentiment from text

    analyzer = SentimentIntensityAnalyzer()
    lst_of_sent = []
    for sentence in final_str:
        vs = analyzer.polarity_scores(sentence)
        for key, item in vs.items():
            if key == 'compound':
                lst_of_sent.append(item)
            elif key=='neg' or key=='pos'or key== 'neu':
                pass
            else:
                return None

    
    df['compound'] = lst_of_sent
    return _helper.publish(df)

        

        
        
