from faker import Faker
import csv
import random

fake = Faker()

departments = ['HR', 'Finance', 'Marketing', 'Information Technology']

def generate_employee_data(num_employees):
    employees = []
    for _ in range(num_employees):
        name = fake.name()
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        department = random.choice(departments)
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
        employees.append([name, hire_date, department, birthday])
    return employees

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Date of hiring', 'Department', 'Date birthday'])
        writer.writerows(data)

if __name__ == "__main__":
    num_employees = 100  
    employee_data = generate_employee_data(num_employees)
    save_to_csv(employee_data, 'data/database.csv')