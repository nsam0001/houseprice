import pandas as pd
import io
import requests

def load_df_from_url(url="https://storage.googleapis.com/nshouseprice/train.csv"):
    """Loads a data frame from a URL. At the moment, the default set is the House Price dataset"""
    url="https://storage.googleapis.com/nshouseprice/train.csv"
    s=requests.get(url).content
    train=pd.read_csv(io.StringIO(s.decode('utf-8')))
    return train

