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
np.zeros(10); np.ones(10); np.full(10);

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


# References

- Python for Data Analysis (McKinney)
