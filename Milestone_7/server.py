from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake employee data
employees = [
    {"id": 1, "name": "John Doe", "birthday": "April 1", "department": "Engineering"},
    {"id": 2, "name": "Patrick Brown", "birthday": "April 10", "department": "Engineering"},
    {"id": 3, "name": "John Wood", "birthday": "April 11", "department": "Engineering"},
    {"id": 4, "name": "Helen King", "birthday": "April 30", "department": "Engineering"},
    {"id": 5, "name": "Jane Smith", "birthday": "April 20", "department": "HR"},
]

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month').capitalize()
    department = request.args.get('department')
    
    # Debugging output
    print(f"Requested Month: {month}, Department: {department}")
    
    filtered_employees = [
        emp for emp in employees 
        if emp['birthday'].startswith(month) and emp['department'] == department
    ]
    
    return jsonify({"total": len(filtered_employees), "employees": filtered_employees})

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    return jsonify({"total": 0, "employees": []}) 

if __name__ == '__main__':
    app.run(port=5000)