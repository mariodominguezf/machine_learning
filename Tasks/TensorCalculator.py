""""
Mario Domínguez Ferrer.
Machine Learning, 4th BA.

TENSOR CALCULATOR.
"""


import torch # To generate tensors
import random  # To be able to generate random numbers


class TensorCalculator:
    # Tensors' dimensions (two dimensions, x and y):
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        return None

    # All-Zeros tensor:
    def tensor_zeros(self):
        return torch.zeros([self.dim_x, self.dim_y])

    # All-Ones tensor:
    def tensor_ones(self):
        return torch.ones([self.dim_x, self.dim_y])

    # Tensor with random values:
    def tensor_random(self):
        return torch.rand([self.dim_x, self.dim_y])

    # Sum of tensors
    def tensor_sum(self):
        a = torch.rand(self.dim_x, self.dim_y) # To generate a random tensor I've used the function 'torch.rand'.
        b = torch.rand(self.dim_x, self.dim_y) # Same here.
        print('Tensor a: \n', a) # Showing the first item of the sum
        print('Tensor b: \n', b) # Showing the second item of the sum
        return torch.add(a, b) # a + b

    # Multiplication of tensors:
    def tensor_multiplication(self):
        # Now we need to generate two tensors but with one condition: the number of rows of tensor c must be equal
        # to the number of columns of tensro d. So:
        c = torch.rand(self.dim_x, self.dim_y)
        d = torch.rand(self.dim_y, self.dim_x)
        print('Tensor c: \n', c) # Showing the first item of the multiplication
        print('Tensor d: \n', d) # showing the second item of the multiplocation
        return torch.matmul(c, d) # c * d

# As I want to generate random dimensions of the tensors, I use the 'random.randint' function for each dimension x & y:
dim_x = random.randint(2, 9) # I choose an interval from 2 to 9 that are going to be the dimensions x of the tensor.
dim_y = random.randint(2, 9) # Same in the other diemsion y.
results = TensorCalculator(dim_x, dim_y) # Generates the tensor with its dimensions in which I will work on.


# Showing the results:
print('All-Zeros Tensor: \n', results.tensor_zeros())
print()
print('All-Ones Tensor: \n', results.tensor_ones())
print()
print('Tensor with random values: \n', results.tensor_random())
print()
print('Sum of tensor a + b: \n', results.tensor_sum())
print()
print('Multiplication of tensor c * d: \n', results.tensor_multiplication())