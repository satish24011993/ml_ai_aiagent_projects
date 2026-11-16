import numpy as np

np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)


random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)

print(np.random.rand(4,4))

print(np.random.randint(1,10,size=(3,3)))