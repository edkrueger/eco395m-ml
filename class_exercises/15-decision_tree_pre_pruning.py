import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from matplotlib import pyplot as plt

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    estimator = DecisionTreeRegressor()
    model = GridSearchCV(estimator=estimator, param_grid={
        # "max_depth": range(1, 10),
        "min_samples_split": np.arange(0, 1, .1),
        # "min_samples_leaf": np.arange(0, 1, .1)
    })

    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    # print(f"{model.intercept_=}")
    print(f"{model.feature_names_in_=}")
    print(f"{model.best_estimator_.feature_importances_=}")
    print(f"{train_mse=}")
    print(f"{test_mse=}")
    
    print(f"{model.best_estimator_.get_depth()=}")
    print(f"{model.best_estimator_.get_n_leaves()=}")

    plt.figure(figsize=(4, 4), dpi=1000)
    plot_tree(model.best_estimator_, feature_names=model.feature_names_in_, filled=True)
    plt.savefig("tree.png")