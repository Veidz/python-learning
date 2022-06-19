# Create a script that reads a product price and shows it's new price with 5% off.
price = float(input('Enter the product price: '))

discount = 0.05
new_price = price * (1 - discount)

print('Product price (5% OFF): {}'.format(new_price))
