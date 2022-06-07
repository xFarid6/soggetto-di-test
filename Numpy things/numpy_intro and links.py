import numpy as np
from numpy import pi

a = np.arange(15).reshape(3, 5)

print(f'{a=},\n {a.shape=}, {a.ndim=}, {a.dtype=}, {a.dtype.name=}')
print(f'{a.itemsize=}, {a.size=}, {type(a)=}')

b = np.array([[1, 2, 3], [4, 5, 6]])
print(f'{b=}')
print(f'{np.zeros((4, 4))=}')
print(f'{np.ones((2, 3, 4), dtype=np.int16)=}')
print(f'{np.empty((2, 3))=}')

print(f'{np.arange(10, 30, 5)=}')
print(f'{np.arange(0, 2, 0.3)=}')


print(f'{np.linspace(0, 2, 9)=}')           # 9 numbers from 0 to 2
x = np.linspace(0, 2 * pi, 100)             # useful to evaluate function at lots of points
f = np.sin(x)

"""     see also:
array, zeros, zeros_like, ones, ones_like, empty, empty_like, 
arange, linspace, numpy.random.Generator.rand, 
numpy.random.Generator.randn, 
fromfunction -> https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction
fromfile -> https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile
"""


# operations on arrays are element-wise (by default i woudl say?)

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(f'{b=}')
c = a - b
print(f'{c=}')

b = b**2
print(f'{b=}')
a = 10 * np.sin(a)
print(f'{a=}')
print(a < 35)


# multiplying matrixes

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A * B)                        # elementwise product

print(A @ B)                        # matrix product

print(A.dot(B))                     # another matrix product


rg = np.random.default_rng(1)       # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)

b += a
print(b)

#! a += b                           # b is not automatically converted to integer type!!!


# simple operations are already implemented
a = rg.random((2, 3))
print(a.sum())

print(a.min())

print(a.max(axis=1))                # the axis parameter specifies the axis you want
                                    # 0 -> columns, 1 -> rows

b = np.arange(12).reshape(3, 4)
print(b)
b.sum(axis=0)                       # sum of each column
b.min(axis=1)                       # min of each row 
b.cumsum(axis=1)                    # cumulative sum along each row


# universal functions

B = np.arange(3)
np.exp(B)
np.sqrt(B)
C = np.array([2., -1., 4.])
np.add(B, C)

"""             See also                ??? GCD, mcm ???
all, any, apply_along_axis, argmax, argmin, argsort, average, 
bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, 
dot, floor, inner, invert, lexsort, max, maximum, mean, median, min, minimum, 
nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, 
vectorize, where
"""


# the ... 
c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
c.shape
c[1, ...]  # same as c[1, :, :] or c[1]
c[..., 2]  # same as c[:, :, 2]


# iterating is done over the first axis, but you cane use array.flat attribute
# to iterate over all the elements in the array
"""                 See also
Indexing on ndarrays, Indexing routines (reference), newaxis, 
ndenumerate, indices
"""


# following three commands all return a modified array, 
# but do not change the original array

a.ravel()  # returns the array, flattened (1 d'ed)
# a.reshape(6, 2)  # returns the array with a modified shape
a.T  # returns the array, transposed
a.T.shape
a.shape

#The reshape function returns its argument with a modified shape, 
# whereas the ndarray.resize method modifies the array itself
# If a dimension is given as -1 in a reshaping operation, 
# the other dimensions are automatically calculated

a = np.arange(10)
b = np.arange(10)
print(np.column_stack((a, b)))


# splitting into smaller arrays
a = np.floor(10 * rg.random((2, 12)))
#array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
#       [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])

# Split `a` into 3
np.hsplit(a, 3)
#[array([[6., 7., 6., 9.],
#       [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
#       [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
#       [1., 8., 1., 0.]])]

# Split `a` after the third and the fourth column
np.hsplit(a, (3, 4))
#[array([[6., 7., 6.],
#      [8., 5., 5.]]), array([[9.],
#       [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
#       [1., 8., 6., 7., 1., 8., 1., 0.]])]


# difference: no copy, shallow copy, deep copy
a = np.arange(int(1e8))
b = a[:100].copy()
del a  # the memory of ``a`` can be released.

"""         ROUTINES                 """
"""
Array creation routines
From shape or value
From existing data
Creating record arrays (numpy.rec)
Creating character arrays (numpy.char)
Numerical ranges
Building matrices
The Matrix class
Array manipulation routines
Basic operations
Changing array shape
Transpose-like operations
Changing number of dimensions
Changing kind of array
Joining arrays
Splitting arrays
Tiling arrays
Adding and removing elements
Rearranging elements
Binary operations
Elementwise bit operations
Bit packing
Output formatting
String operations
String operations
Comparison
String information
Convenience class
C-Types Foreign Function Interface (numpy.ctypeslib)
Datetime Support Functions
numpy.datetime_as_string
numpy.datetime_data
Business Day Functions
Data type routines
numpy.can_cast
numpy.promote_types
numpy.min_scalar_type
numpy.result_type
numpy.common_type
numpy.obj2sctype
Creating data types
Data type information
Data type testing
Miscellaneous
Optionally SciPy-accelerated routines (numpy.dual)
Linear algebra
FFT
Other
Mathematical functions with automatic domain (numpy.emath)
Functions
Floating point error handling
Setting and getting error handling
Internal functions
Discrete Fourier Transform (numpy.fft)
Standard FFTs
Real FFTs
Hermitian FFTs
Helper routines
Background information
Implementation details
Type Promotion
Normalization
Real and Hermitian transforms
Higher dimensions
References
Examples
Functional programming
numpy.apply_along_axis
numpy.apply_over_axes
numpy.vectorize
numpy.frompyfunc
numpy.piecewise
NumPy-specific help functions
Finding help
Reading help
Input and output
NumPy binary files (NPY, NPZ)
Text files
Raw binary files
String formatting
Memory mapping files
Text formatting options
Base-n representations
Data sources
Binary Format Description
Linear algebra (numpy.linalg)
The @ operator
Matrix and vector products
Decompositions
Matrix eigenvalues
Norms and other numbers
Solving equations and inverting matrices
Exceptions
Linear algebra on several matrices at once
Logic functions
Truth value testing
Array contents
Array type testing
Logical operations
Comparison
Masked array operations
Constants
Creation
Inspecting the array
Manipulating a MaskedArray
Operations on masks
Conversion operations
Masked arrays arithmetic
Mathematical functions
Trigonometric functions
Hyperbolic functions
Rounding
Sums, products, differences
Exponents and logarithms
Other special functions
Floating point routines
Rational routines
Arithmetic operations
Handling complex numbers
Extrema Finding
Miscellaneous
Matrix library (numpy.matlib)
numpy.matlib.empty
numpy.matlib.zeros
numpy.matlib.ones
numpy.matlib.eye
numpy.matlib.identity
numpy.matlib.repmat
numpy.matlib.rand
numpy.matlib.randn
Miscellaneous routines
Performance tuning
Memory ranges
Array mixins
NumPy version comparison
Utility
Matlab-like Functions
Exceptions
Padding Arrays
numpy.pad
Polynomials
Transitioning from numpy.poly1d to numpy.polynomial
Documentation for the polynomial Package
Documentation for Legacy Polynomials
Random sampling (numpy.random)
Quick Start
Introduction
Concepts
Features
Set routines
numpy.lib.arraysetops
Making proper sets
Boolean operations
Sorting, searching, and counting
Sorting
Searching
Counting 
"""