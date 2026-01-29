import pandas as pd
from matplotlib import pyplot as plt

from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns").values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    results = []
    for k in range(1, len(X_train + 1)):

        model = KNeighborsRegressor(n_neighbors=k)
        
        model.fit(X_train, y_train)
        y_hat_train = model.predict(X_train)
        y_hat_test = model.predict(X_test)

        train_mse = mean_squared_error(y_train, y_hat_train)
        test_mse = mean_squared_error(y_test, y_hat_test)

        result = {
            "k": k,
            "neg_train_mse": -train_mse,
            "neg_test_mse": -test_mse
        }

        results.append(result)

    df = pd.DataFrame(results).head(30)
    df.set_index("k").plot.line()
    plt.grid()
    plt.savefig("knn_complexity_plot.png")


