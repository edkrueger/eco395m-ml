import pandas as pd

from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns").values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    transformer = StandardScaler()

    transformer.fit(X_train)

    X_train_scaled = transformer.transform(X_train)
    X_test_scaled = transformer.transform(X_test)


    model = KNeighborsRegressor(n_neighbors=5)


    model.fit(X_train_scaled, y_train)
    y_hat_train = model.predict(X_train_scaled)
    y_hat_test = model.predict(X_test_scaled)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(train_mse)
    print(test_mse)
    