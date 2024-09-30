import csv
from datetime import datetime
import argparse

def generate_report(filename, month, verbose):
    birthdays = {}
    anniversaries = {}

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hire_date = datetime.strptime(row['Date of hiring'], '%Y-%m-%d')
            birthday = datetime.strptime(row['Date birthday'], '%Y-%m-%d')

            # Calculating birthday 
            if birthday.month == month:
                if row['Department'] in birthdays:
                    birthdays[row['Department']].append(row['Name'])
                else:
                    birthdays[row['Department']] = [row['Name']]
            
            # Calculating anniversaries
            if hire_date.month == month:
                if row['Department'] in anniversaries:
                    anniversaries[row['Department']].append(row['Name'])
                else:
                    anniversaries[row['Department']] = [row['Name']]

    print(f"Report for {month} generated")
    print("--- Birthdays ---")
    print(f"Total: {sum(len(names) for names in birthdays.values())}")
    print("By department:")
    for dept, names in birthdays.items():
        print(f"- {dept}: {len(names)}")
        if verbose:
            print(f"  Names: {', '.join(names)}")

    print("--- Anniversaries ---")
    print(f"Total: {sum(len(names) for names in anniversaries.values())}")
    print("By department:")
    for dept, names in anniversaries.items():
        print(f"- {dept}: {len(names)}")
        if verbose:
            print(f"  Names: {', '.join(names)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate employee report.")
    parser.add_argument('filename', type=str, help='Path to the database CSV file')
    parser.add_argument('month_name', type=str, help='Name of the month')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    month_mapping = {
        "January": 1, "February": 2, "March": 3,
        "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "December": 12
    }

    month_number = month_mapping.get(args.month_name.capitalize())
    
    if month_number is None:
        print("Invalid month name.")
    else:
        generate_report(args.filename, month_number, args.verbose)