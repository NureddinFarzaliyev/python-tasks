import numpy as np

# Cretaes 4 length arr of zeros
a = np.zeros(6)
a.shape = (2, 3)

# empty array
b = np.empty(10)

# creates an arr from list specified in parameter
c = np.array([1, 2, 3])

# random array from 0 to 10 with size of 6
d = np.random.randint(10, size=6)


print(d)