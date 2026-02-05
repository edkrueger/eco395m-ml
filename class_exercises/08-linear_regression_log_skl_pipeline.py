import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import TransformedTargetRegressor

def safe_log(x):
    return np.log(x + 1)

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


    estimator = make_pipeline(FunctionTransformer(func=safe_log), LinearRegression())
    model = TransformedTargetRegressor(regressor=estimator, func=np.log, inverse_func=np.exp)

    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(f"{model.regressor_[-1].intercept_=}")
    print(f"{model.regressor_[-1].feature_names_in_=}")
    print(f"{model.regressor_[-1].coef_=}")
    print(f"{train_mse=}")
    print(f"{test_mse=}")
    