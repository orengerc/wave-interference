"""
Holds equations used for fitting
"""

import numpy as np
import cmath


def linear_no_intercept(x, a):
    return a * x


def linear(x, a, b):
    return a * x + b


def parabolic_no_intercept(x, a, b):
    return a * (x ** 2) + b * x


def parabolic(x, a, b, c):
    return a * (x ** 2) + b * x + c


def one_over_x(x, a, b):
    return a / x + b


def one_over_x_no_intercept(x, a):
    return a / x


def exp(x, a, b):
    return a * np.exp(b / x)


def cos_squared(x, I_0, phi):
    return I_0 * (np.cos(x + phi) ** 2)
