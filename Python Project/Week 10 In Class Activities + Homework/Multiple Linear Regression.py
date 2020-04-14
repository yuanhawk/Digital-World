import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


def multiple_linear_regression(b, x_index, y_index, order, size, seed):
    # Step 1
    xdata = b.data[:, np.newaxis, x_index]
    ydata = b.data[:, np.newaxis, y_index]

    # Step 2 refer to: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
    poly = PolynomialFeatures(order, include_bias=False)
    x_data = poly.fit_transform(xdata)

    # Step 3
    x_train, x_test, y_train, y_test = train_test_split(x_data, ydata, test_size=size, random_state=seed)

    # Step 4,5 refer to: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    # Step 6, coefficients, intercept, mean-squared error and the r2
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results = {'coefficients': regr.coef_, 'intercept': regr.intercept_, 'mean squared error': mse, 'r2 score': r2}

    return x_train[:,[0]], y_train[:,[0]], x_test[:,[0]], y_pred[:,[0]], results