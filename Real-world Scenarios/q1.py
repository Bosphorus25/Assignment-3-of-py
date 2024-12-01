# Write a function that takes a list of employee salaries and calculates the average salary.
def employ_salary():
    total_employee = int(input("enter total num of employees: "))
    saleries = []
    for i in range(total_employee):
        salery = int(input("enter salery: "))
        saleries.append(salery)
    sum_all = sum(saleries)
    average = sum_all / total_employee
    print(average)
employ_salary()