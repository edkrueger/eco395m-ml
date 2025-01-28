import numpy as np

class DummyRegressor():

    def fit(self, X, y):
        self.mean = np.mean(y)

    def predict(self, X):
        return self.mean

if __name__ == "__main_":
    
    X = np.array([[1],[2], [2]])
    y = np.array([1, 2, 4])

    y_hat_expected = np.array([7/3, 7/3, 7/3])

    model = DummyRegressor()
    model.fit(X, y)
    y_hat_observed = model.predict(X)

    assert (y_hat_expected == y_hat_observed).all()


