# Employee Management System

## 1. Project Overview

This Employee Management System is a Python-based application that demonstrates advanced database operations using MySQL. It showcases complex SQL queries, including joins and subqueries, as well as data visualization capabilities. The system allows users to manage employee data, perform various types of searches, and generate reports.

## 2. Project Files

- `db.conf`: Configuration file for database connection settings
- `db.py`: Module for handling database connections
- `employee.py`: Core module containing employee management functions and complex queries
- `program.py`: Main program file that runs the application
- `test_mysql_connection.py`: Script to test the database connection
- `requirements.txt`: List of Python package dependencies
- `employee_management.log`: Log file for the application
- `sql/ddl.sql`: SQL file containing Data Definition Language statements
- `sql/dml.sql`: SQL file containing Data Manipulation Language statements

## 3. How to Run

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your MySQL database and update the `db.conf` file with your database credentials.
4. Run the SQL scripts in the `sql` folder to set up your database schema and initial data:
   ```
   mysql -u your_username -p < sql/ddl.sql
   mysql -u your_username -p < sql/dml.sql
   ```
5. Run the main program:
   ```
   python program.py
   ```

## 4. Steps

When you run the program, you'll be presented with a menu of options:

- L - List All Employees
- A - Add New Employee
- E - Edit Employee
- D - Delete Employee
- C - View Salary Chart
- X - Advanced Search (including custom SQL)
- S - Department Summary
- Q - Exit

Choose an option by entering the corresponding letter.

## 5. Requirements

- Python 3.x
- MySQL database
- Python packages (see `requirements.txt`):
  - mysql-connector-python
  - matplotlib

## Features

- Complex database queries using joins and subqueries
- Data visualization with matplotlib
- Comprehensive error handling and logging
- Advanced search capabilities
- Department summary reports

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).
