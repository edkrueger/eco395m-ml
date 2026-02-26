import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import StackingRegressor


if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


    lr = make_pipeline(StandardScaler().set_output(transform="pandas"), PolynomialFeatures(degree=1, include_bias=False).set_output(transform="pandas"), LinearRegression())


    poly_reg = GridSearchCV(
        estimator=lr,
        scoring="neg_mean_squared_error",
        param_grid={
            "polynomialfeatures__degree": list(range(1, 10))
        }
    )

    decision_tree = DecisionTreeRegressor()

    model = StackingRegressor(estimators=[("poly_reg", poly_reg), ("decision_tree", decision_tree)])

    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    # print(model.best_params_)
    # print(f"{model.best_estimator_[-1].intercept_=}")
    # print(pd.Series(dict(zip(model.best_estimator_[-1].feature_names_in_, model.best_estimator_[-1].coef_))))
    print(f"{train_mse=}")
    print(f"{test_mse=}")
    