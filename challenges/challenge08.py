# Create a script that reads a value in meters and shows it converted into centimeters and milimeters.
meter = float(input('Type a value (meter): '))

centimeter = meter * 100
milimiter = meter * 1000

print('Centimeter: {}, Milimeter: {}'.format(centimeter, milimiter))
