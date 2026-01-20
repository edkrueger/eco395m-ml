import numpy as np

def calc_r_2(y, y_hat):
    y = np.array(y)
    y_hat = np.array(y_hat)

    ss_total = ((y - y.mean()) ** 2).sum()
    ss_reg = ((y - y_hat) ** 2).sum()

    r_2 = (ss_total - ss_reg) / ss_total

    return r_2

def calc_mse(y, y_hat):
    y = np.array(y)
    y_hat = np.array(y_hat)

    return ((y - y_hat) ** 2).mean()


def linear_regression(X, y):

    X = np.array(X)
    print(X)
    y = np.array(y)

    X = np.hstack((
        np.ones(len(X)).reshape(-1, 1), X
        ))

    print(X)

    beta = np.linalg.inv(X.T @ X) @ X.T @ y

    y_hat = X @ beta
    r_2 = calc_r_2(y, y_hat)
    mse = calc_mse(y, y_hat)

    return beta, y_hat, r_2, mse


if __name__ == "__main__":

    y = [1, 2, 3]
    y_hat_1 = [2, 2, 2]
    y_hat_2 = [1, 2, 3]
    y_hat_3 = [1, 2, 4]

    r_2_1 = 0
    r_2_2 = 1
    r_2_3 = 1 / 2

    mse_1 = 2 / 3
    mse_2 = 0
    mse_3 = 1 / 3

    assert calc_r_2(y, y_hat_1) == r_2_1
    assert calc_r_2(y, y_hat_2) == r_2_2
    assert calc_r_2(y, y_hat_3) == r_2_3


    assert calc_mse(y, y_hat_1) == mse_1
    assert calc_mse(y, y_hat_2) == mse_2
    assert calc_mse(y, y_hat_3) == mse_3

    X = [[1], [2], [3]]
    y = [1, 2 , 3]

    res = linear_regression(X, y)
    print(res)



