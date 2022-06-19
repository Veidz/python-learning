# Create a script that reads a product price and shows it's new price with 5% off.
price = float(input('Enter the product price: '))

new_price = price * 0.95

print('Product price (5% OFF): {}'.format(new_price))
