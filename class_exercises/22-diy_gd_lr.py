import warnings

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


def gradient_descent(df, gamma, x0, tol=10**-3, max_iter=1000):
    
    n_iter = 0
    x_last = np.inf
    x_current = x0

    while np.abs(x_current - x_last).all() >= tol:

        # print(f"{n_iter=}, {x_current=}")

        if n_iter >= max_iter:
            warnings.warn(f"Did not converge after {n_iter=}!")
            return x_current, n_iter


        x_next = x_current - gamma * df(x_current)

        x_last = x_current
        x_current = x_next

        n_iter = n_iter + 1

    return x_current, n_iter

def add_intercept(X):
    return np.hstack((np.ones(len(X)).reshape(-1, 1), X))

class GDLinearRegression():

    def __init__(self, learning_rate=.001, fit_intercept=True, max_iter=1000):

        self.learning_rate = learning_rate
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter

    def fit(self, X, y):


        X = np.array(X)
        y= np.array(y)

        if self.fit_intercept:
            X = add_intercept(X)

        df = lambda beta: -2 * X.T @ y + 2 * X.T @ X @ beta

        beta, n_iter = gradient_descent(
            df=df,
            gamma=self.learning_rate,
            x0=np.zeros(X.shape[1]),
            max_iter=self.max_iter
        )

        print(f"{n_iter=}")

        self.beta= beta
    
    def predict(self, X):

        if self.fit_intercept:
            X = add_intercept(X)

        return X @ self.beta

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    model = GDLinearRegression(learning_rate=.0000001, max_iter=1_000_000)

    model.fit(X_train, y_train)

    print(f"{model.beta=}")
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    print(f"{y_hat_test=}")

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    # print(f"{model.intercept_=}")
    # print(f"{model.feature_names_in_=}")
    # print(f"{model.coef_=}")
    print(f"{train_mse=}")
    print(f"{test_mse=}")
    