import numpy as np

# Creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

#print("Array monodimensionale:",arr,"\nArray bidimensionale:",arr2d)
print("Array monodimensionale:",arr,"\n")
print("Array bidimensionale:",arr2d,"\n")

arra = np.array([1, 2, 3, 4, 5])

# Indexing
print(arra[0]) # Output: 1

# Slicing
print(arra[1:3]) # Output: [2 3]

# Boolean Indexing
print(arr[arr > 2]) # Output: [3 4 5]

arr_2d = np.array([1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12])

# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[5 6 7 8]
                   #           9 10 11 12]
                               
# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]
