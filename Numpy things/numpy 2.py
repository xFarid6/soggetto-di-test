import numpy as np

# sort and concatenate

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)

""" See also

argsort, which is an indirect sort along a specified axis,
lexsort, which is an indirect stable sort on multiple keys,
searchsorted, which will find elements in a sorted array, and
partition, which is a partial sort.

more on sort: https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort
"""

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)

#np.reshape(a, newshape=(1, 6), order='C')   # C - C-like, 
                                            # F - fortran-like, 
                                            # A - fortran-like if a is fortran contiguous in memory

"""  approfondimento - situazioni particolari
You can also use np.nonzero() to select elements or indices from an array.

Starting with this array:

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
You can use np.nonzero() to print the indices of elements that are, for example, 
less than 5:

b = np.nonzero(a < 5)
print(b)
(array([0, 0, 0, 0]), array([0, 1, 2, 3]))

In this example, a tuple of arrays was returned: one for each dimension. 
The first array represents the row indices where these values are found, 
and the second array represents the column indices where the values are found.

numpy.nonzero(a)[source]
Return the indices of the elements that are non-zero.

Returns a tuple of arrays, one for each dimension of a, 
containing the indices of the non-zero elements in that dimension. 
The values in a are always tested and returned in row-major, C-style order.
"""

# random number generator
rng.integers(5, size=(2, 4))
# read more: https://numpy.org/doc/stable/reference/random/index.html#numpyrandom

# unique elements
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)

unique_values, indices_list = np.unique(a, return_index=True)   # get indices of first occurence.
print(indices_list)


unique_values, occurrence_count = np.unique(a, return_counts=True)  # get the frequency count of unique values
print(occurrence_count)

# transiposing
arr = np.arange(6).reshape((2, 3))
print(arr)
arr.transpose()
print(arr)

# flipping
print('Reversed array: ', arr.flip(arr))

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)

reversed_arr_rows = np.flip(arr_2d, axis=0)
print(reversed_arr_rows)

arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)

arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)


# ravel and flatten
x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x.flatten()     # preferrable as doesnt modify the parent array
a2 = x.ravel()


# MEAN SQUARE ERROR
error = (1 / n) * np.sum( np.square( predictions - labels ) )
