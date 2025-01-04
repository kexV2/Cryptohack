from sympy import isprime

power_list = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

# find all three digit prime numbers
three_digit_primes = [num for num in range(100, 1000) if isprime(num)]

# iterate through each number
for prime in three_digit_primes:
    # iterate through all possible values of x
    for base in range(1, prime):
        

        # make sure the pattern works
        for index, value in enumerate(power_list):
            if index == len(power_list) - 1:

                # print the result if the pattern is valid
                print(f'crypto{{{prime},{base}}}')
            elif (base * value) % prime != power_list[index + 1]:
                break
