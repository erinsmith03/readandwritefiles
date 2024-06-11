import csv

employees=open('employee_data.csv','r')
employee_file=csv.reader(employees)

next(employee_file)
for rec in employee_file:
    name=rec[1]
    salary=float(rec[3])
    bonus=float(rec[7])
    bonus_amount=bonus*salary
    pay=salary+bonus
    print(f'Name:{name}','\n',f'Salary:${salary:,.2f}','\n',f'Bonus:${bonus_amount:,.2f}','\n',f'Pay:${pay:,.2f}','\n','\n')



