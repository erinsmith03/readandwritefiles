import csv

customers=open('customers.csv','r')
customer_file=csv.reader(customers) #need to create customer csv object

outfile=open('customer_country.csv','w')

outfile.write('Full Name,Country\n') #writing out first header
next(customer_file) #skip header of the file

counter =0

for rec in customer_file:
    fname=rec[1] #object for the index of first name
    lname=rec[2] #object for the index of last name 
    country=rec[4] #object for the index of country
    fullname=fname+''+lname #object for full name concatenated

    outfile.write(fullname + ',' + country + '\n') #writing to our outfile
    counter+=1

outfile.close()

print(f'Total Number of customers is: {counter}')


        

    