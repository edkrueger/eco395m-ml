import numpy as np

def add_intercept(X):
    X = np.array(X)
    return np.hstack((np.ones(len(X)).reshape(-1, 1), X))

class LinearRegression():

    def __init__(self, fit_intercept=True):
        self.include_intercept = fit_intercept

    def fit(self, X, y):

        X = np.array(X)
        y = np.array(y)

        if self.include_intercept:
            X = add_intercept(X)

        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X):

        if self.include_intercept:
            X = add_intercept(X)
            
        return X.dot(self.beta)

if __name__ == "__main__":
    
    X = np.array([[1], [2], [3]])
    assert np.array_equal(add_intercept(X), np.array([[1, 1], [1, 2], [1, 3]]))


    X = np.array([[1],[2], [3]])
    y = np.array([1, 2, 3])

    model = LinearRegression()
    model.fit(X, y)
    y_hat_observed = model.predict(X)

    print("hello")
    print(model.beta)

    assert np.allclose(y, y_hat_observed)


