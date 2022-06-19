# Create a script that reads the user balance (BRL) and shows it how many dollars (USD) the person can buy.
user_balance = float(input('Type your balance: (BRL) '))

current_usd = 5.15

print('New balance (USD): {:.2f}'.format(user_balance / current_usd))
