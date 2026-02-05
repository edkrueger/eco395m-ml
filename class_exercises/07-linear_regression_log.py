import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    raw_df = pd.read_csv("data/advertising.csv").set_index("id")
    
    print(raw_df.min())
    print(raw_df["radio"].sort_values(ascending=True))
    

    df = raw_df.drop(128, axis="rows")
    y = df["sales"].values
    X = df.drop("sales", axis="columns")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    X_train = np.log(X_train)
    X_test = np.log(X_test)
    y_train_log = np.log(y_train)
    y_test_log = np.log(y_test)


    model = LinearRegression()

    model.fit(X_train, y_train_log)
    y_hat_train_log = model.predict(X_train)
    y_hat_test_log = model.predict(X_test)

    y_hat_train = np.exp(y_hat_train_log)
    y_hat_test = np.exp(y_hat_test_log)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(f"{model.intercept_=}")
    print(f"{model.feature_names_in_=}")
    print(f"{model.coef_=}")
    print(f"{train_mse=}")
    print(f"{test_mse=}")
    