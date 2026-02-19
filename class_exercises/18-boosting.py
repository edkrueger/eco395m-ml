import numpy as np
import pandas as pd

# from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

from matplotlib import pyplot as plt

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    estimator = GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=.1)

    model = GridSearchCV(estimator=estimator, param_grid={
        "n_estimators": list(range(1, 200)),
        "max_depth": [1, 2, 3],
        "learning_rate": np.arange(.00001, 1, 20)
    }, n_jobs=-1)


    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)
    
    print(f"{model.best_params_=}")
    print(f"{train_mse=}")
    print(f"{test_mse=}")