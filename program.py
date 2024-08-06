#Import our database library
import db
# Import the employee module
import employee

# You must install the driver for mysql
# pip install mysql-connector-python

# Get the database configuration
config = db.getConfig()
# Connect to the database
connection = db.connect(config)
# Create a cursor
# cursor = connection.cursor()
# Execute the query
# cursor.execute("SHOW DATABASES;")

# for d in cursor:
    # print (d)
choice = ""
while (choice != "q"):

    choice = input("Please enter an option:\n'L' - List All Employees\n'A' - ADD New Employee\n'E' - Edit Employee\n'D' - Delete Employee\n'C' - view Salary Chart\n'X' - CUSTOM Search(Including custom SQL queries)\n'S' - Department Summary \n'Q' - EXIT:").lower()

    match choice:

        case "l":
            employee.list_employees(connection)

        case "a":
            employee.insert_employee(connection) 

        case "e":
            employee.edit_employee(connection)
        case "d":
            employee.delete_employee(connection)

        case "x":
            employee.complex_search(connection)

        case "c":
            employee.generate_chart(connection)

        case "s":
            employee.department_summary(connection)

        case "q":
            print ("Thank you, come again!")

        case _:
            print("Invalid option. Please try again.")

