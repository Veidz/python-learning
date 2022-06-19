# Create a script that reads a number and show its double, triple and square root.
num = int(input('Type a number: '))

double = num * 2
triple = num * 3
square_root = num ** (1/2)

print('Number: {}, Double: {}, Triple: {}, Square root: {}'.format(num, double, triple, square_root))
