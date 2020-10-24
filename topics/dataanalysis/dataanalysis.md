    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# Data Analysis
> Personal Notes

# Index

- [NumPy](#numpy)
- [Pandas](#pandas)
- [Matplotlib](#matplotlib)

## NumPy

__Features__ <br>

- array/vector computation.
- ndarray - compact array data-structure.
- operations on entire array without loops.
- r/w arrays from/to disk as memory-mapped files (directly memory addressing).
- linear algebra, random numbers, F-transform.
- a C-API to connect to computational C/C++, Fortran libraries.

__Basics__ <br>

```py
import numpy as np

# Array: Basics
data = [[1,2,3],2,3]
_array = np.array(data)
_array.ndim; _array.shape; _array.dtype;

# Array: Initialization
np.zeros(10); np.ones(10); np.full(10,1);

# NumPy equivalent of Python's range()
np.arange(start, stop, step)

# Array: Type Conversion
_array.astype(np.float64)
_strings = np.array(['1.25','2.0','3.2'], dtype=np.string_)
_strings.astype(float)

# Array: Arithmetic (same-size arrays)
_array + _array; _array - _array; _array * _array; _array / _array;
1/_array; _array ** 0.5;
_array1 = np.ones(10); _array2 = np.ones(10);
_array1 > _array2; _array1 < _array2; _array1 == _array2; _array1 is _array2;

# Array: Arithmetic (different-size arrays - "broadcasting")
```

- Array Slicing

In Python, slicing creates a new Object (list, array, ...). <br>
In NumPy, slicing operates on the original ndarray. <br>
To create a new object using slicing, use copy(). <br>

```py
_array = np.zeros(10,dtype='uint8') # Array of 8-bit values
_array[5:] = 1			    # Same array
_array[5:].copy()		    # New array
```

- Array Indexing [[1]](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.html), [[2]](https://numpy.org/devdocs/user/basics.indexing.html) <br>
At times, it's necessary to access certain values from a matrix. How does this fit in with an ndarray? <br>
We can use indexing to address this. <br>

```py
# 0-D array
array0D = np.array(8)

# 1-D array, shape-(3,)
array1D = np.array([2.3, 0.1, -9.1])

# 2-D array, shape-(3, 2)
array2D = np.array([[93, 95],
          [84, 100],
          [99, 87]])

# 3-D array, shape-(2, 2, 2)
array3D = np.array([[[0, 1],
           [2, 3]],
          [[4, 5],
           [6, 7]]])

array1D[:]         = 1          # Sets array1D[0-2] = 1
array2D[:][0]      = 1          # Replaces first element in 2D array with a scalar value of 1
array2D[:][-1]     = -1         # Replaces last element in 2D array with a scalar value of 1
array2D[:][1:]     = np.ones(2) # Replaces elements (2nd onward) in 2D array with unit-valued entries
array3D[:][:][-1]  = [1,1]      # Replaces last value of every element with [1,1]
```




# References

- Python for Data Analysis (McKinney)
