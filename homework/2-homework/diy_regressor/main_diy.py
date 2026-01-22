import numpy as np
from knn import KNeighborsRegressor

def mean_squared_error(y, y_hat):
    return((y - y_hat) ** 2).mean()

if __name__ == "__main__":

    train = np.loadtxt("data/advertising_train.csv", delimiter=",", skiprows=1)

    id_train = train[:, 0]
    X_train = train[:, 1:-1]
    y_train = train[:, -1]

    test = np.loadtxt("data/advertising_test.csv", delimiter=",", skiprows=1)
    id_test = test[:, 0]
    X_test = test[:, 1:-1]
    y_test = test[:, -1]

    # should work with any of these
    model = KNeighborsRegressor(n_neighbors=1)

    model.fit(X_train, y_train)
    
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(f"{train_mse=}")
    print(f"{test_mse=}")