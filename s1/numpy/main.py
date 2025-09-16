import numpy as NP

arr = NP.array([[1, 8], [1, 2], [3, 7], [6, 3]], dtype="float32")
print(arr)
arr = NP.where(arr % 2 == 0, "zoj", arr)
print(arr)
print(NP.__version__)
arr = arr.reshape((2, 4))
print(arr)
print(arr.ndim)
print(arr.dtype)
print(f"size= {arr.size}")
print(f"new array= {NP.arange(0, 100, 3.2, "float32")}")
print(f"new array= {NP.linspace(0, 100, 5, dtype=int)}")
print(f"array ones=\n {NP.ones(shape=(3, 3))}")
print(f"array zeros=\n {NP.zeros(shape=(3, 3))}")
print(f"array full=\n {NP.full((3, 3), 66)}")
print(f"array random=\n {(NP.random.rand(3, 3)*10).round()}")
print(arr.shape)

# operator in arrays

array1 = NP.array([[1, 3], [4, 5]], dtype="float32")
array2 = NP.array([[3, 2], [7, 8]], dtype="float32")

print(f"sum array= \n {NP.add(array1,array2)}")
print(f"multi array= \n {NP.multiply(array1,array2)}")
print(f"division array= \n {NP.divide(array1,array2)}")

print(array2.flatten())
print(array2.ravel())

print(f"concat array=\n {NP.concat([array1,array2])}")