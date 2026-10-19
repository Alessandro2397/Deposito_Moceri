import numpy as np

# Primo array: numeri interi da 18 a 49
array1 = np.arange(18, 50)

# Secondo array: numeri interi da 18 a 49
array2 = np.arange(18, 50)

# Verifica del tipo di dato e della forma
print("Primo array:", array1)
print("dtype:", array1.dtype)
print("shape:", array1.shape)

print("\nSecondo array:", array2)
print("dtype:", array2.dtype)
print("shape:", array2.shape)

# Converto il tipo di dato in float
array1 = array1.astype(np.float64)
print("Tipo di dato di array1:",array1.dtype,"\n")

# Stampo la forma dell'array
print("Forma dell'array:",array1.shape,"\n")
