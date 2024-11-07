numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# What the below code will do is convert the numbers and then assemble them in order
# and get rid of any spaces between the code resulting in the flag being shown
print(''.join(map(chr, numbers)))