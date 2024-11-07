
def extendedGCD(a, b): 
    if a == 0: 
        return b, 0, 1
    gcd, x1, y1 = extendedGCD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

p = 26513
q = 32321

# GCD and u, v
gcd, u, v = extendedGCD(p, q)

print("GCD:", gcd)      
print("u:", u)
print("v:", v)

# resources used to help https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/