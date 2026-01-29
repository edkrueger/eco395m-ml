import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.dummy import DummyRegressor
from sklearn.svm import SVR

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns").values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # model = DummyRegressor(strategy="median")
    # # model = KNeighborsRegressor(n_neighbors=5)
    model = LinearRegression()
    
    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(train_mse)
    print(test_mse)