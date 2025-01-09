"""
This logic was taken from https://www.youtube.com/watch?v=uuvF7QwE3Ew
"""

import numpy as np


# Performs modular multiplication of matrices.
def modular_mult(matrix1, matrix2):
    res = (matrix1.dot(matrix2)) % q

    return res


# Performs modular addition of matrices.
def modular_add(matrix1, matrix2):
    res = (matrix1 + matrix2) % q

    return res


# Performs modular subtraction of matrices.
def modular_sub(matrix1, matrix2):
    res = (matrix1 - matrix2) % q

    return res


""" 
n is number of rows and colums of "A" matrix.
k is the number of colums of "s", "e" and "t".
q must be prime and it is our Field. 
"""

# General inputs.
n = 4
k = 1
q = 13

""" 
"A" and "t" are public values. "s" and "e" are private values.
Alice shares "A" and "t" with Bob. 
"""

# Alice's inputs.
# Lattice Base of Alice.
A = np.array([[4, 1, 11, 10], [5, 5, 9, 5], [3, 9, 0, 10], [1, 3, 3, 2]])

# Secret value of Alice.
s = np.array([[6], [9], [11], [11]])

# Error value of Alice.
e = np.array([[0], [-1], [1], [1]])

# KeyGen() by Alice.
t = modular_mult(A, s)
t = modular_add(t, e)
print("t:\n", t)

"""
Bob takes Alice's "A" and "t" values and finds "u" and "v" values.
He chooses random "r" and small noise values "e1" and "e2" with a message "m".
Performs computation and sends "u" and "v" to Alice for she can find secret shared "m".
"""

# Bob's inputs.
r = np.array([12, 5, 10, 0])
e1 = np.array([1, 0, 0, -1])
e2 = np.array([-1])
m = np.array([1])

# Enc() by Bob.
# Bob calculates "u".
u = modular_mult(r, A)
u = modular_add(u, e1)
print("\n u:", u)


# Bob calculates "v".
v = modular_mult(r, t)
v = modular_add(v, e2)
v = modular_add(v, m)
print("\n v:", v)

"""
Alice receive the values "u" and "v".
She performs computation for finding secret shared "m".
"""
# Dec() by Alice.
f1 = modular_mult(u, s)
f2 = modular_sub(v, f1)
print("\n f2:", f2)

if f2[0] > (q / 2):
    f2[0] = 1
else:
    f2[0] = 0


def result(f2, m):

    if f2[0] == m:
        return True
    else:
        return False


print("\n", result(f2, m))
