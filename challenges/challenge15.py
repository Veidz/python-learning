# Create a script that reads the total km driven by a rental car and the total days it was rented.
# Calculate the price to pay, knowing that the car costs $60 per day and $0.15 per km.
qnt_km = float(input('Enter the total km driven: '))
qnt_days = int(input('Enter the total days of rent: '))

cost_day = 60
cost_km = 0.15

total_cost = (qnt_days * cost_day) + (qnt_km * cost_km)

print(f'Total cost: ${total_cost:.2f}')
