class Employee:
    def __init__(self, emp_id, name, position, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
        self.bonus = 0
        self.deductions = 0

    def calculate_salary(self):
        base_salary = self.hourly_rate * self.hours_worked
        gross_salary = base_salary + self.bonus
        net_salary = gross_salary - self.deductions
        return {
            "Base Salary": base_salary,
            "Bonus": self.bonus,
            "Deductions": self.deductions,
            "Net Salary": net_salary
        }

    def generate_salary_slip(self):
        salary = self.calculate_salary()
        print("\n--- Salary Slip ---")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Position   : {self.position}")
        for k, v in salary.items():
            print(f"{k:15}: ${v:.2f}")
        print("-------------------\n")


# Payroll system core
class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        hourly_rate = float(input("Enter Hourly Rate: "))
        self.employees[emp_id] = Employee(emp_id, name, position, hourly_rate)

    def enter_work_details(self, emp_id):
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            emp.hours_worked = float(input("Enter Hours Worked: "))
            emp.bonus = float(input("Enter Bonus: "))
            emp.deductions = float(input("Enter Deductions: "))
        else:
            print("Employee not found!")

    def generate_slip(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].generate_salary_slip()
        else:
            print("Employee not found!")


# Main
def main():
    payroll = PayrollSystem()
    while True:
        print("\n--- Payroll Management System ---")
        print("1. Add Employee")
        print("2. Enter Work Details")
        print("3. Generate Salary Slip")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            payroll.add_employee()
        elif choice == "2":
            emp_id = input("Enter Employee ID: ")
            payroll.enter_work_details(emp_id)
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            payroll.generate_slip(emp_id)
        elif choice == "4":
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
