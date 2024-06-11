import csv

sales=open('sales.csv','r')
sales_file=csv.reader(sales,delimiter=',')


outfile=open('salesreport.csv','w')
outfile.write('Customer | Total\n')

next(sales_file)

sales_list={}

for rec in sales_file:
    customer=rec[0]
    subtotal=float(rec[3])

    if customer in sales_list:
        sales_list[customer] += subtotal
    else:
        sales_list[customer]=subtotal

for cust, amount in sales_list.items():
    outfile.write(f'{cust}|{amount:.2f}\n')

#we need to read each line, and print only one of each ID, and add the total amount per that ID


