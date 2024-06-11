import csv

# open the csv file in read mode
customers = open('customers.csv','r')

# using the csv library, create a csv object
# the delimiter ',' tells the program how the columns are seperated
customer_file = csv.reader(customers, delimiter=',')

# skip the first line in the csv file if it contains a header record
# in this file it would be "ID,FirstName,LastName,City,Country,Phone"
next(customer_file)


# using a for loop you can step through the file, one line at a time
for record in customer_file:
    # this print statement shows that the variable record is a list
    # and each element in the list corresponds to each column in the
    # file
    print(record)
    
    # so to access the second element or second column of the current line
    # you just need to use the corresponding index value
    print('first name:',record[1])
    print('last name:',record[2])
    print('City:',record[3])
    print('Country:',record[4])
    print('Phone:',record[5])

    # this command will pause the program until a key is pressed
    input()
    




