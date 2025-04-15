import numpy as np

def add_intercept(X):
    X = np.array(X)
    return np.hstack((np.ones(len(X)).reshape(-1, 1), X))

def logistic(z):
    return 1 / (1 + np.exp(-z))

def gd(df, x_0, learning_rate, max_iter=1000, tol=10**-6):

    x_last = np.inf
    x_current = x_0
    n_iter = 0

    while np.abs(x_current - x_last).all() > tol:

        # print(f"{n_iter=}")
        # print(f"{x_current=}")
        # print(f"{df(x_current)=}")

        if n_iter >= max_iter:
            print("Did not converge to tolerance")
            break

        x_current, x_last = x_current - learning_rate * df(x_current), x_current
        n_iter += 1
    
    return x_current, n_iter

class LogisticRegression():

    def __init__(self, learning_rate=.01, fit_intercept=True, tol=10**-6, max_iter=1000):
        self.include_intercept = fit_intercept
        self.tol = tol
        self.max_iter = max_iter 
        self.learning_rate = learning_rate

    def fit(self, X, y):

        X = np.array(X)
        y = np.array(y)

        if self.include_intercept:
            X = add_intercept(X)

        beta, n_iter = gd(
            df=lambda beta: -(X.T @ (y - logistic(X @ beta))) / X.shape[0],
            learning_rate=self.learning_rate,
            max_iter=self.max_iter,
            x_0=np.ones(X.shape[1]))
        
        self.beta = beta

    def predict_proba(self, X):

        if self.include_intercept:
            X = add_intercept(X)
            
        return logistic(X.dot(self.beta))
    
    def predict(self, X, threshold=.5):
        return self.predict_proba(X) > threshold