-- Insert sample data
INSERT INTO department (department_name, location) VALUES
('HR', 'New York'),
('IT', 'San Francisco'),
('Finance', 'Chicago');

INSERT INTO project (project_name, start_date, end_date, budget) VALUES
('Website Redesign', '2023-01-01', '2023-06-30', 100000.00),
('ERP Implementation', '2023-03-01', '2024-02-29', 500000.00),
('Marketing Campaign', '2023-05-01', '2023-12-31', 250000.00);

INSERT INTO employee (first_name, last_name, salary, employee_type, department_id) VALUES
('John', 'Doe', 95000.00, 'Manager', 1),
('Jane', 'Smith', 65000.00, 'Administrator', 2),
('Bob', 'Johnson', 55000.00, 'Operational', 3),
('Alice', 'Williams', 120000.00, 'Manager', 2),
('Charlie', 'Brown', 60000.00, 'Administrator', 1),
('Karlotte', 'Gauson', 50000.00, 'Operational', 1),
('Melanie','Smith', 110000.00,'Manager', 3),
('Walid','Khalil', 90000.00, 'Administrator', 3),
('Sanmeet','Kaur', 60000.00,'Operational', 1),
('Stephan', 'Todd', 50000.00, 'Operational', 2),
('Alex', 'Souza', 80000.00, 'Administrator', 2),
('Paulie', 'John', 75000.00, 'Operational', 3);

INSERT INTO employee_project (employee_id, project_id) VALUES
(1, 2), (2, 1), (3, 3), (4, 2), (5, 3), (6,1), (7,3), (8,3),(9,1), (10,2), (11,2),(12,3);