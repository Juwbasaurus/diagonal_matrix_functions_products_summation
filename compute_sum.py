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
    # Construct list of possible function results
    F_before = [f_before(x) for x in X]
    F_after = [f_after(x) for x in X]
    G_before= [g_before(x) for x in X]
    G_after = [g_after(x) for x in X]

    # Initialize empty vectors for function sums at thresholds (0 is at trshld == x_0, 1 at x_1 etc.)
    F = []
    G = []
    for threshold in range(len(X)):
        F.append(np.sum(F_before[:threshold] + F_after[threshold:]))
        G.append(np.sum(G_before[:threshold] + G_after[threshold:]))

    return np.dot(F, G)


if __name__ == '__main__':
    print(compute_sum([1, 2, 3]))
