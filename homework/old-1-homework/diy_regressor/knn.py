import numpy as np

# students to implement
class KNeighborsRegressor():

    def __init__(self, n_neighbors):
        pass
    
    def fit(self, X, y):
        pass        

    def predict(self, X):
        pass
    
if __name__ == "__main__":

    X = np.array([[1], [2], [4]])
    y = np.array([1, 2, 4])

    model = KNeighborsRegressor(n_neighbors=1)
    model.fit(X, y)
    assert (model.predict(X) == np.array([1, 2, 4])).all()

    model = KNeighborsRegressor(n_neighbors=2)
    model.fit(X, y)
    assert (model.predict(X) == np.array([3/2, 3/2, 6/2])).all()

    model = KNeighborsRegressor(n_neighbors=10**9)
    model.fit(X, y)
    assert (model.predict(X) == np.array([7/3, 7/3, 7/3])).all()




