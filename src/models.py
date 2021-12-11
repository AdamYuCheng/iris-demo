from sklearn.linear_model import LogisticRegression
from config.cfg import C

def model_fit(df, X, y):
    clf = LogisticRegression(C=C)
    clf.fit(df[X], df[y])
    return clf