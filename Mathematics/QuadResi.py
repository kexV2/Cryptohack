# Parameters
p = 29
ints = [14, 6, 11]

# Check to see what above numbers are Quadratic Residues
for x in ints:
    for a in range(p):
        if (a * a) % p == x:  # Check to see if a^2 ≡ x (mod p)
            print(f"x = {x} is a quadratic residue, smallest root is {a}")