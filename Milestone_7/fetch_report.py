import requests
import sys

if len(sys.argv) < 3:
    print("Usage: python fetch_report.py <month> <department>")
    sys.exit(1)

month = sys.argv[1]
department = sys.argv[2]

response = requests.get(f'http://127.0.0.1:5000/birthdays?month={month}&department={department}')

if response.status_code == 200:
    data = response.json()
    print(f"Report for {department} department for {month} fetched.")
    print(f"Total: {data['total']}")
    print("Employees:")
    for emp in data['employees']:
        print(f"- {emp['birthday']}, {emp['name']}")
else:
    print("Error fetching report.")