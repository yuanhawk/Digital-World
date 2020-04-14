import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def linear_regression(b, x_index, y_index, size, seed):
    # Step 2
    xdata = b.data[:, np.newaxis, x_index]
    ydata = b.data[:, np.newaxis, y_index]

    # Step 3
    x_train, x_test, y_train, y_test = train_test_split(xdata, ydata, test_size=size, random_state=seed)

    # Step 4,5 refer to: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    # Step 6, coefficients, intercept, mean-squared error and the r2
    # mse: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
    # r2: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results = {'coefficients': regr.coef_, 'intercept': regr.intercept_, 'mean squared error': mse, 'r2 score': r2}

    return x_train, y_train, x_test, y_pred, results