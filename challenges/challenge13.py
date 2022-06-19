# Create a script that reads an employee's salary and shows it with 15% raise.
salary = float(input('Enter the employee salary: '))

salary_raise = 0.15
new_salary = salary * (1 + salary_raise)

print('New salary: {}'.format(new_salary))
