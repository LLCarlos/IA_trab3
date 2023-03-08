import numpy as np


def compute_mse(theta_0, theta_1, data)
    mse = 0.0
    size = len(data)
    for d in data:
        y_hat = theta_0 + (d[0] * theta_1)
        mse = mse + pow((d[1] - y_hat), 2)

    mse = mse/size

    return mse


def step_gradient(theta_0, theta_1, data, alpha):
    df_d0 = 0.0
    df_d1 = 0.0

    for d in data:
        h0 = theta_0 + (d[0]*theta_1)
        df_d0 = df_d0 + (h0 - d[1])*1
        df_d1 = df_d1 + (h0 - d[1])*d[0]

    df_d0 = (2*df_d0)/len(data)
    df_d1 = (2*df_d1)/len(data)

    theta_0 = theta_0 - alpha*df_d0
    theta_1 = theta_1 - alpha*df_d1

    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    thetas_0 = []
    thetas_1 = []

    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        thetas_0.append(theta_0)
        thetas_1.append(theta_1)

    return thetas_0, thetas_1
