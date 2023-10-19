import torch  #Importante!

my_tensor = torch.zeros(5)
print(my_tensor)

my_tensor = torch.ones(5,4) # 5 filas, 4 columnas
print(my_tensor)

my_tensor = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]]) # Cada [] es una fila
print(my_tensor)
print(my_tensor[:]) # Hace lo mismo que arriba
print(my_tensor[1:]) # Elimina la primera fila. O mejor dicho, empieza a imprimir por la segunda fila
print(my_tensor[1:,:]) # Lo mismo
print(my_tensor[0,:]) # Solo imprime la primera fila
print(my_tensor[-1,0])  # Imprime de la última gila, el primer valor

a = torch.ones(3,2) # Matriz de unos de tres filas y dos columnas
a_t = torch.transpose(a,0,1) # ALtera el orden y pasa de (3,2) a (2,3), dos filas y tres columnas
# a_t = a.transpose(0,1) -> Otra forma de hacerlo
print(a_t)
print(a)
print(a.shape, a_t.shape)

a = torch.tensor([2.0, 3.0, 4.0, 1.0])
b = torch.tensor([2.0, -2.0, 3.0, 7.0])
result = a + b
print(result)

a = torch.tensor([[2.0], [3.0], [4.0], [1.0]])
b = torch.tensor([[5.0],[-2.0], [3.0], [7.0]])
result = a + b
print(result)

# Escalado de matrices
a = torch.tensor([1,2])
b = torch.tensor([2,3])
print(torch.dot(a,b))

# Multiplicación de matrices
a = torch.tensor([[1,2],[3,2]])
b = torch.tensor([[3,4], [3,4]])
print(torch.matmul(a,b))

# Multiplicación de matrices con distintas medidas
# Para que se pueda hacer, la primera matriz tiene que tener las mismas columnas que filas la segunda matriz.
c = torch.tensor([1,2])
d = torch.tensor([[3,4],[3,4]])
print(torch.matmul(d,c))