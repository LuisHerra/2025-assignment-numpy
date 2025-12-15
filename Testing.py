import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8]])

def max_value(arr): 
    return np.max(arr) 

def max_index(arr): 
    for i in range(arr.shape[0]): 
        for j in range(arr.shape[1]): 
            if (max_value(arr2) == arr[i][j]): 
                return i, j 

print(max_value(arr))
print(max_value(arr2))
print(max_index(arr2))


