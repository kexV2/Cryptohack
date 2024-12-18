from sympy import mod_inverse

# Given values
g = 209  # The number we want the inverse of
p = 991  # The modulus


d = mod_inverse(g, p)
print(d)  


# got help from https://docs.python.org/3/library/functions.html#pow