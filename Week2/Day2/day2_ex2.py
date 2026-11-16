import numpy as np

arr = np.array([1,2,3,4,5,6])

even = arr[arr%2==0]
print('even',even)

arr[arr < 3] = 0
print('less than 3',arr)

# Generate random dataset
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)


# calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))