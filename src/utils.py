import pandas as pd

def read_data(path):
    '''讀取訓練資料'''
    df = pd.read_csv(path)
    return df