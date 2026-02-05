import pandas as pd

from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


if __name__ == "__main__":

    df = pd.read_csv("data/advertising.csv").set_index("id")
    y = df["sales"].values
    X = df.drop("sales", axis="columns").values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    estimator = make_pipeline(StandardScaler(), KNeighborsRegressor())

    print(estimator)

    model = GridSearchCV(
        estimator=estimator,
        scoring="neg_mean_squared_error",
        param_grid={
            "kneighborsregressor__n_neighbors": list(range(1, 30))
        }
    )

    model.fit(X_train, y_train)
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)

    train_mse = mean_squared_error(y_train, y_hat_train)
    test_mse = mean_squared_error(y_test, y_hat_test)

    print(model.best_params_)
    print(train_mse)
    print(test_mse)
    