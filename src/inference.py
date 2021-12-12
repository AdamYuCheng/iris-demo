from utils import load_model, read_data
from config.cfg import *


def inference():
    print('Start to model inference.')

    # 讀取模型
    clf = load_model(MODEL_PATH)

    # 讀取預測資料 from csv or db
    df = read_data(INFERENCE_DATA)

    # 模型預測
    y_pred = clf.predict(df[X])

    # 存取預測結果
    df['pred'] = y_pred
    df.to_csv(PREDICT_PATH, index=False)
    print('Inference finish.')


if __name__ == '__main__':
    inference()