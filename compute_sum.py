import numpy as np
from functions import f_before, f_after, g_before, g_after


def compute_sum(X):
    """
    Given a list X of datapoints x_0 to x_n, applies functions f(.) and g(.) to each element.
    The functions come in two flavors, the flavor is chosen wrt a threshold: if x >= threshold, functions f_after and
    g_after are used, otherwise f_before and g_before.
    Each datapoint iteratively becomes a threshold, at each step the respective functions are applied to each element
    of X.
    For each pair f_i(x) and g_j(x) (i,j are both from 0 to n-1) a product is calculated. Then the sum of all products
    is found.

    First, it applies each function to each element of X, constructing a respective list for each function.
    Then, it finds sums of all possible thresholds: e.g. for threshold == x_0, we apply f_after to each element of the
    list X, and sum it up; for threshold == x_3, f_before is applied to x_0, x_1,x_2, for others -- f_after, sum it up.
    Thanks to lists of precomputed functions, we can simply pick needed elements from them.

    Then it takes dot product between sums over function f and sums over function g.

    Args:
      X: a list of data points (ints)
    Returns:
      sum of products of all possible functions' products wrt to thresholds.
    """
    # Construct lists of partial sums on every x as threshold
    F_before_cumsums = [0]
    cur_sum = 0
    for x in X[:-1]:
        cur_sum += f_before(x)
        F_before_cumsums.append(cur_sum)
    i = len(X) - 1
    cur_sum = 0
    F_after_cumsums = [0] * len(X)
    for i in range(len(X)-1, -1, -1):
        cur_sum += f_after(X[i])
        F_after_cumsums[i] = cur_sum

    G_before_cumsums = [0]
    cur_sum = 0
    for x in X[:-1]:
        cur_sum += g_before(x)
        G_before_cumsums.append(cur_sum)
    i = len(X) - 1
    cur_sum = 0
    G_after_cumsums = [0] * len(X)
    for i in range(len(X)-1, -1, -1):
        cur_sum += g_after(X[i])
        G_after_cumsums[i] = cur_sum

    # Initialize empty vectors for function sums at thresholds (0 is at trshld == x_0, 1 at x_1 etc.)
    # Sum at each threshold is the sum of left subarray (which is cumsum of f_before to each element)
    # and sum of right subarray in this point
    F, G = [], []
    for threshold in range(len(X)):
        F.append(F_before_partsums[threshold] + F_after_partsums[i])
        G.append(G_before_partsums[threshold] + G_after_partsums[i])

    return np.dot(F, G)


if __name__ == '__main__':
    print(compute_sum([1, 2, 3]))
