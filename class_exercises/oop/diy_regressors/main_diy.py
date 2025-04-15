import numpy as np

from dummy_regressor import DummyRegressor
from linear_regression import LinearRegression
from gd_regressor import GDRegression


def mean_squared_error(y, y_hat):
    return ((y - y_hat) ** 2).mean()

if __name__ == "__main__":

    train = np.loadtxt("data/advertising_train.csv", delimiter=",", skiprows=1)

    id_train = train[:, 0]
    X_train = train[:, 1:-1]
    y_train = train[:, -1]

    test = np.loadtxt("data/advertising_test.csv", delimiter=",", skiprows=1)
    id_test = test[:, 0]
    X_test = test[:, 1:-1]
    y_test = test[:, -1]

    # model = DummyRegressor()
    # model = LinearRegression()
    model = LinearRegression()
    # model = GDRegression(
    #     max_iter=1000000,
    #     learning_rate=.0000001,
    #     tol=10**-3)
    model.fit(X_train, y_train)
    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(train_mse)
    print(test_mse)