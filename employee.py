import logging
from mysql.connector import Error

logging.basicConfig(filename='employee_management.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
#This function will list the employees
def list_employees(conn):
    try:    
        #Get a cursor
        list_employees_cursor = conn.cursor()
    
        list_query = """SELECT employee_id, 
                        first_name,
                        last_name,
                        salary,
                        employee_type
                            FROM employee;"""
    
        list_employees_cursor.execute(list_query)


        for x in list_employees_cursor:
            print (x)
        logging.info(f"Listed all employees")

    except Error as e:
        print(f"Error listing employees: {e}")
        logging.error(f"Error listing employees: {e}")


# This function will insert an employee
def insert_employee(conn):
    #prompt the user for the required information
    try:
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        salary = input("Please enter the salary for the user")
        employee_type = input("Please enter the employee type (Manager, Administrator, Operational)")

        insert_employee_query = """INSERT INTO employee (first_name, last_name, salary, employee_type)
                                VALUES (%s, %s, %s, %s)"""

        employee_values = ( first_name, last_name, float(salary), employee_type )
        insert_employee_cursor = conn.cursor() 

        insert_employee_cursor.execute(insert_employee_query, employee_values)

        conn.commit()

        print("Employee inserted successfully.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        logging.warning(f"Invalid input during employee insertion: {ve}")
    except Error as e:
        print(f"Error inserting employee: {e}")
        logging.error(f"Error inserting employee: {e}")
        conn.rollback()

# This function will edit an employee
def edit_employee(conn):
    employee_id = input("Please enter the employee ID to edit: ")
    
    # First, check if the employee exists
    check_query = "SELECT * FROM employee WHERE employee_id = %s"
    check_cursor = conn.cursor()
    check_cursor.execute(check_query, (employee_id,))
    
    if check_cursor.fetchone() is None:
        print("Employee not found.")
        return


    # If employee exists, prompt for new information
    first_name = input("Enter new first name (press enter to keep current): ")
    last_name = input("Enter new last name (press enter to keep current): ")
    salary = input("Enter new salary (press enter to keep current): ")
    employee_type = input("Enter new employee type (Manager, Administrator, Operational) (press enter to keep current): ")

    # Prepare the update query
    update_query = "UPDATE employee SET "
    update_values = []

    if first_name:
        update_query += "first_name = %s, "
        update_values.append(first_name)
    if last_name:
        update_query += "last_name = %s, "
        update_values.append(last_name)
    if salary:
        update_query += "salary = %s, "
        update_values.append(float(salary))
    if employee_type:
        update_query += "employee_type = %s, "
        update_values.append(employee_type)

    # Remove the trailing comma and space
    update_query = update_query.rstrip(', ')

    update_query += " WHERE employee_id = %s"
    update_values.append(employee_id)

    # Execute the update query
    update_cursor = conn.cursor()
    update_cursor.execute(update_query, tuple(update_values))
    conn.commit()

    print("Employee updated successfully.")

# This function will delete an employee
def delete_employee(conn):
    employee_id = input("Please enter the employee ID to delete: ")
    
    # First, check if the employee exists
    check_query = "SELECT * FROM employee WHERE employee_id = %s"
    check_cursor = conn.cursor()
    check_cursor.execute(check_query, (employee_id,))
    
    if check_cursor.fetchone() is None:
        print("Employee not found.")
        return

    # If employee exists, confirm deletion
    confirm = input(f"Are you sure you want to delete employee {employee_id}? (y/n): ")
    
    if confirm.lower() == 'y':
        delete_query = "DELETE FROM employee WHERE employee_id = %s"
        delete_cursor = conn.cursor()
        delete_cursor.execute(delete_query, (employee_id,))
        conn.commit()
        print("Employee deleted successfully.")
    else:
        print("Deletion cancelled.")

# This function will filter employees based on 3 options
def complex_search(conn):
    print("Complex Employee Search")
    print("1. Search by Salary Range:")
    print("2. Search by Employee Type:")
    print("3. Search by name:")
    print("4. Custom Search Using MySQL Query ")
    
    choice = input("Enter your choice (1-4) and Press Enter: ")

    search_cursor = conn.cursor()
    
    if choice == '1':
        min_salary = float(input("Enter minimum salary: "))
        max_salary = float(input("Enter maximum salary: "))
        search_query = """SELECT * FROM employee 
                          WHERE salary BETWEEN %s AND %s 
                          ORDER BY salary DESC"""
        search_cursor.execute(search_query, (min_salary, max_salary))

    elif choice == '2':
        emp_type = input("Enter employee type (Manager, Administrator, Operational): ")
        search_query = """SELECT * FROM employee 
                          WHERE employee_type = %s 
                          ORDER BY salary DESC"""
        search_cursor.execute(search_query, (emp_type,))

    elif choice == '3':
        name = input("Enter name to search: ")
        search_query = """SELECT * FROM employee 
                          WHERE first_name LIKE %s OR last_name LIKE %s 
                          ORDER BY last_name, first_name"""
        search_cursor.execute(search_query, (f'%{name}%', f'%{name}%'))

    elif choice == '4':
            print("Custom SQL Query")
            print("CAUTION: This allows direct SQL input. Use with care.")
            custom_query = input("Enter your SQL query: ")
            
            # Basic security check
            if any(keyword in custom_query.lower() for keyword in ['delete', 'drop', 'truncate', 'insert', 'update']):
                raise ValueError("Data modification queries are not allowed in custom search.")
            
            search_cursor.execute(custom_query)


    else:
        print("Invalid choice.")
        return


    results = search_cursor.fetchall()
    if results:
        for row in results:
            print(row)
            print("\n")
    else:
        print("No results found.")


import matplotlib.pyplot as plt


# This function will generate average salary chart by employee type
# using matplotlib and generates png file to save the chart.
def generate_chart(conn):

    cursor = conn.cursor()
    query = """SELECT employee_type, AVG(salary) as avg_salary
                FROM employee
                GROUP BY employee_type"""
    cursor.execute(query)
    data = cursor.fetchall()
        
    employee_types = [row[0] for row in data]
    avg_salaries = [row[1] for row in data]
        
    plt.figure(figsize=(10, 5))
    plt.bar(employee_types, avg_salaries)
    plt.title('Average Salary by Employee Type')
    plt.xlabel('Employee Type')
    plt.ylabel('Average Salary')
        
    plt.show()
        


def department_summary(conn):
    try:
        cursor = conn.cursor()
        query = """
        SELECT 
            d.department_name,
            COUNT(e.employee_id) as employee_count,
            AVG(e.salary) as avg_salary,
            SUM(e.salary) as total_salary,
            (SELECT COUNT(*) FROM employee_project ep
             JOIN employee e2 ON ep.employee_id = e2.employee_id
             WHERE e2.department_id = d.department_id) as project_involvements
        FROM department d
        LEFT JOIN employee e ON d.department_id = e.department_id
        GROUP BY d.department_id
        ORDER BY employee_count DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("\nDepartment Summary:")
        print("Department | Employees | Avg Salary | Total Salary | Project Involvements")
        print("-" * 75)
        for row in results:
            print(f"{row[0]:<12} | {row[1]:<9} | ${row[2]:<10.2f} | ${row[3]:<12.2f} | {row[4]}")
        
        logging.info("Generated department summary")
    except Error as e:
        print(f"Error generating department summary: {e}")
        logging.error(f"Error generating department summary: {e}")


