import numpy as np
# from sklearn.linear_model import LogisticRegression
from logistic_regression import LogisticRegression
# from sklearn.metrics import confusion_matrix

def confusion_matrix(y_true, y_pred):

    predicted_true_idxs = y_pred == 1
    predicted_false_idxs = y_pred == 0
    true_idxs = y_true == 1
    false_idxs = y_true == 0

    true_negatives = (false_idxs & predicted_false_idxs).sum()
    false_positives = (false_idxs & predicted_true_idxs).sum()
    false_negatives = (true_idxs & predicted_false_idxs).sum()    
    true_positives = (true_idxs & predicted_true_idxs).sum()

    print(f"{true_negatives=}")
    print(f"{false_positives=}")
    print(f"{false_negatives=}")
    print(f"{true_positives=}")
    
    return [[true_negatives, false_positives], [false_negatives, true_positives]]




if __name__ == "__main__":

    train = np.loadtxt("data/caravan_train.csv", delimiter=",", skiprows=1)

    id_train = train[:, 0]
    X_train = train[:, 1:-1]
    y_train = train[:, -1]

    test = np.loadtxt("data/caravan_test.csv", delimiter=",", skiprows=1)
    id_test = test[:, 0]
    X_test = test[:, 1:-1]
    y_test = test[:, -1]

    # should work with any of these
    # model = LogisticRegression(max_iter=10000, C=10000)
    model = LogisticRegression(fit_intercept=True, learning_rate=.01, max_iter=100000, tol=10**-18)

    model.fit(X_train, y_train)
    
    y_hat_train = model.predict(X_train, threshold=.33)
    y_hat_test = model.predict(X_test, threshold=.33)

    train_confusion_matrix = confusion_matrix(y_train, y_hat_train)
    test_confusion_matrix = confusion_matrix(y_test, y_hat_test)

    print(f"{train_confusion_matrix=}")
    print(f"{test_confusion_matrix=}")
    
    try:
        print(f"{model.coef_}")
        print(f"{model.intercept_}")
    except:
        pass

    try:
        print(model.beta)
    except:
        pass