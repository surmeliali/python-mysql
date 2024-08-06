-- Drop the database if it exists and recreate it
DROP DATABASE IF EXISTS employees_db;
CREATE DATABASE employees_db;
USE employees_db;

-- Create the department table
CREATE TABLE department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Create the project table
CREATE TABLE project (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2)
);

-- Modify the employee table to include department_id
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2),
    employee_type ENUM('Manager', 'Administrator', 'Operational'),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

-- Create a junction table for employee-project relationship
CREATE TABLE employee_project (
    employee_id INT,
    project_id INT,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    PRIMARY KEY (employee_id, project_id)
);