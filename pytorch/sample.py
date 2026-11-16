import torch

tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)

# Perform matrix multiplication
result = torch.matmul(tensor_a, tensor_b)

# Print the tensors and the result
print("Tensor A:")
print(tensor_a)
print("\nTensor B:")
print(tensor_b)
print("\nResult of Matrix Multiplication:")
print(result)
