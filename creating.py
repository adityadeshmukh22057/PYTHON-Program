import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 2, 8, 5, 9],
                [7, 3, 9, 6, 10]])  # Added one element
print("Array:\n", arr)
print("Type:", type(arr))
print("Length:", len(arr))
print("Shape:", arr.shape)
print("Slice:", arr[0, 1:3], arr[1, 2:5], arr[2, 1:4])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
