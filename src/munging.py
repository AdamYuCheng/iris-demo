import pandas as pd


def training_data_munging(df):
    '''資料清理'''
    df_cleaned = fill_null_data(df)
    return df


def fill_null_data(df):
    '''補空值'''
    df_filled = df.fillna(0)
    return df_filled