import numpy as np

class DummyRegressor():

    def fit(self, X, y):

        self.mean = np.mean(y)
    
    def _predict_one(self, x):

        return self.mean
    
    def predict(self, X):
        return [self._predict_one(x) for x in X]
    
if __name__ == "__main__":
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([1, 2, 4])

    model = DummyRegressor()
    model.fit(X, y)
    assert (model.predict(X) == np.array([7 / 3, 7 / 3, 7 / 3])).all()