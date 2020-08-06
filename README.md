#  The gist

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

# Structure

- compute_sum.py : imports functions and computes the sum of products of function combinations at thresholds.
- functions.py : defines the 4 functions used

# How to use

Either run the compute_sum.py, changing the arguments to compute_sum function, or import the compute_sum function from the file.
