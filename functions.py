import numpy as np


def f_before(x):
    """
    Applies a function to a data point.
    This function is applied to elements before the threshold.

    Args:
      x : a data point (int)

    Returns:
      the result of applying function to x (int)
    """
    return np.power(x, 2)


def f_after(x):
    """
    Applies a function to a data point.
    This function is applied to elements after or at the threshold.

    Args:
      x : a data point (int)

    Returns:
      the result of applying function to x (int)
    """
    return x + 5


def g_before(x):
    """
    Applies a function to a data point.
    This function is applied to elements before the threshold.

    Args:
      x : a data point (int)

    Returns:
      the result of applying function to x (int)
    """
    return 2


def g_after(x):
    """
    Applies a function to a data point.
    This function is applied to elements after or at the threshold.

    Args:
      x : a data point (int)

    Returns:
      the result of applying function to x (int)
    """
    return 3 * x
