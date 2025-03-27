import numpy as np

def add_intercept(X):
    X = np.array(X)
    return np.hstack((np.ones(len(X)).reshape(-1, 1), X))

def gd(df, x_0, learning_rate, max_iter=1000, tol=10**-6):

    x_last = np.inf
    x_current = x_0
    n_iter = 0

    while np.abs(x_current - x_last).all() > tol:

        print(f"{n_iter=}")
        print(f"{x_current=}")
        print(f"{df(x_current)=}")

        if n_iter >= max_iter:
            print("Did not converge to tolerance")
            break

        x_current, x_last = x_current - learning_rate * df(x_current), x_current
        n_iter += 1
    
    return x_current, n_iter

class GDRegression():

    def __init__(self,learning_rate=.01, fit_intercept=True, tol=10**-6, max_iter=1000):
        self.include_intercept = fit_intercept
        self.tol = tol
        self.max_iter = max_iter 
        self.learning_rate = learning_rate

    def fit(self, X, y):

        X = np.array(X)
        y = np.array(y)

        if self.include_intercept:
            X = add_intercept(X)

        beta, n_iter = gd(df=lambda beta: -2 * X.T @ y + 2 * X.T @ X @ beta, learning_rate=self.learning_rate, max_iter=self.max_iter, x_0=np.zeros(X.shape[1]))

        print(n_iter)

        self.beta = beta

    def predict(self, X):

        if self.include_intercept:
            X = add_intercept(X)
            
        return X.dot(self.beta)

if __name__ == "__main__":
    
    X = np.array([[1], [2], [3]])
    assert np.array_equal(add_intercept(X), np.array([[1, 1], [1, 2], [1, 3]]))


    X = np.array([[1],[2], [3]])
    y = np.array([1, 2, 3])

    model = GDRegression()
    model.fit(X, y)
    y_hat_observed = model.predict(X)

    print("hello")
    print(model.beta)

    print(y_hat_observed)

    assert np.allclose(y, y_hat_observed)


