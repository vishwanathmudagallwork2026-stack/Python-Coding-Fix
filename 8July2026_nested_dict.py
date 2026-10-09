"""Work with nested dictionaries representing employee records."""

company = {
    "emp1": {"empid": 3, "ename": "Zaraki", "salary": 80_000, "dept": "Accounts"},
    "emp2": {"empid": 34, "ename": "Picallo", "salary": 10_000, "dept": "Coaching"},
    "emp3": {"empid": 45, "ename": "Ramesh", "salary": 45_000, "dept": "Sales"},
}

# Give a raise only to employees whose salary exceeds 30,000.
for employee_id, employee in company.items():
    if employee["salary"] > 30_000:
        employee["salary"] += 10_000
    print(employee_id, employee["ename"], employee["salary"])
