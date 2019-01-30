"""
Train Application
"""


from sklearn import linear_model


def train():
    reg = linear_model.LinearRegression()
    reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    return reg.coef_
