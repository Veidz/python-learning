# Create a script that reads two numbers and shows the sum of them.
num1 = int(input('Type a number: '))
num2 = int(input('Type another one: '))

sum = num1 + num2

# print('The sum of', num1 + ' + ' + num2, 'is', sum)
print('The sum of {} + {} is {}'.format(num1, num2, sum))
