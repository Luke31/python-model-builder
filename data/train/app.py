"""
Train Application.

Load data and train.
"""


from joblib import dump

import pandas as pd

from sklearn import linear_model


def train(trainingsetpath: str, modelpath: str):
    """
    Train model using trainingset and save model in modelpath using joblib.

    :type modelpath: str
    :type trainingsetpath: str
    :param trainingsetpath: path to input-file
    :param modelpath: path to folder for output-file
    """
    trainingset = pd.read_csv(trainingsetpath)
    y = trainingset.pop('y').values
    x = trainingset
    model = train_model(x, y)
    dump(model, modelpath)


def train_model(x, y):
    """
    Train model using training-set x with target variable y.

    :param x: training-set with features (m, n)
    :param y: target-variable (m)
    :return:
    """
    reg = linear_model.LinearRegression()
    reg.fit(x, y)
    return reg
