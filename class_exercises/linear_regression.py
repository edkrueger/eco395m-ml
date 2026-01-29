import numpy as np


def add_intercept(X):
    return np.hstack((np.ones(len(X)).reshape(-1, 1), X))

class LinearRegression():

    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept

    def fit(self, X, y):

        X = np.array(X)
        y= np.array(y)

        if self.fit_intercept:
            X = add_intercept(X)

        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    def predict(self, X):

        if self.fit_intercept:
            X = add_intercept(X)

        return X @ self.beta
    
if __name__ == "__main__":

    X = [[1], [2], [3]]
    y = [1, 2 , 3]
    model = LinearRegression()

    model.fit(X, y)
    y_hat = model.predict(X)
    assert np.allclose(y, y_hat)

    X = [[1], [2], [3]]
    y = [2, 3, 4]
    model = LinearRegression()
    model.fit(X, y)
    y_hat = model.predict(X)
    assert np.allclose(y, y_hat)

    X = [[1], [2], [3]]
    y = [2, 3, 4]
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    y_hat = model.predict(X)
    assert not np.allclose(y, y_hat)