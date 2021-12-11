import pandas as pd
import pickle


def read_data(path):
    '''讀取訓練資料'''
    df = pd.read_csv(path)
    return df


def save_model(clf, path):
    with open(path, 'wb') as f:
        pickle.dump(clf, f)


def load_model(path):
    with open(path, 'rb') as f:
        clf = pickle.load(f)
    return clf
