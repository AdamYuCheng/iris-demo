from utils import read_data, save_model
from munging import training_data_munging
from models import model_fit
import pickle
from sklearn.metrics import accuracy_score
from config.cfg import *


def train():
    '''模型訓練主程式'''

    # 讀取資料
    df = read_data(TRAINING_DATA)

    # 資料前處理
    df_cleaned = training_data_munging(df)

    # 模型訓練
    clf = model_fit(df_cleaned, X, Y)
    print(f'Model training finish.')

    # 存取模型
    save_model(clf, MODEL_PATH)
    print(f'Model {MODEL_PATH} saved finish.')

    # 驗證結果
    y_pred = clf.predict(df_cleaned[X])
    score = accuracy_score(df[Y], y_pred)
    print(f'Training score: {score:.2f} .')


if __name__ == '__main__':
    train()