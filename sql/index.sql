-- Active: 1738313813024@@127.0.0.1@5432@postgres
CREATE DATABASE "adv-sql"

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO employees VALUES
(1, 'Alice', 'Engineering', 95000, '2020-01-15'),
(2, 'Bob', 'Marketing', 82000, '2019-03-22'),
(3, 'Charlie', 'Engineering', 105000, '2021-06-01'),
(4, 'Diana', 'Sales', 75000, '2022-09-10'),
(5, 'Evan', 'Marketing', 88000, '2020-11-05'),
(6, 'Fiona', 'Engineering', 115000, '2018-12-03');


CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    emp_id INT,
    amount DECIMAL(10,2),
    sale_date DATE,
    region VARCHAR(50)
);

INSERT INTO sales VALUES
(101, 4, 15000, '2023-01-05', 'West'),
(102, 4, 22000, '2023-01-12', 'East'),
(103, 2, 8500, '2023-02-03', 'North'),
(104, 5, 43000, '2023-02-15', 'South'),
(105, 4, 17000, '2023-03-01', 'West'),
(106, 6, 29000, '2023-03-10', 'East');


SELECT * from sales;

-- Query 1: Find the average salary of employees in each department
SELECT department, Round(AVG(salary),2) as average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;

-- Query 2: Find the top 3 highest-paid employees in each department
SELECT department, emp_name, salary
FROM employees
GROUP BY department ,emp_name,salary 
ORDER BY salary DESC 
LIMIT 3;

-- Query 3: Find the number of sales made by each employee in each region in the last quarter
SELECT e.emp_name,s.region , count(*) as total_sales
from employees as e
JOIN sales as s  on e.emp_id=s.emp_id
WHERE s.sale_date>=date_trunc('QUARTER',current_timestamp) - INTERVAL '3 months'
GROUP BY e.emp_name, s.region
ORDER BY total_sales DESC;

-- Query 4: Find the total sales amount for each region in the last quarter
SELECT region , SUM(amount) as total_sales_amount
FROM sales
WHERE sale_date>=date_trunc('QUARTER',current_timestamp) - INTERVAL '3 months'
GROUP BY region
ORDER BY total_sales_amount DESC;

-- Query 5: Find the average sales amount per employee in each region in the last quarter
SELECT e.emp_name, s.region , AVG(amount) as average_sales_amount
FROM employees as e
JOIN sales as s  on e.emp_id=s.emp_id
WHERE s.sale_date>=date_trunc('QUARTER',current_timestamp) - INTERVAL '3 months'
GROUP BY e.emp_name, s.region
ORDER BY average_sales_amount DESC;



-- Query 6: Find the number of employees in each department with a salary greater than the average salary of all employees
SELECT department, COUNT(*) as num_employees ,round(avg(salary),2)
FROM employees
where salary>(select avg(salary) from employees)
GROUP BY department
ORDER BY num_employees DESC;

-- Query 7: Find the employees who have been with the company for more than 5 years
SELECT emp_name, hire_date
FROM employees
WHERE hire_date<=current_date - INTERVAL '5 years';


-- Common Table Expressions (CTEs)
-- CTEs are temporary result sets that exist within a query.
--  They improve readability and enable recursive queries.
WITH EngineeringTeam AS (
    SELECT emp_name, salary
    FROM employees
    WHERE department = 'Engineering'
)
SELECT round(AVG(salary),2) AS avg_engineering_salary
FROM EngineeringTeam;

SELECT emp_name from employees where department='Engineering';

-- Window Functions
-- Window functions allow you to perform calculations across a set of rows,
--  partitioned by a specified column or expression.
--  They are commonly used in conjunction with aggregate functions.
SELECT emp_name, department, salary,
AVG(salary) OVER (PARTITION BY department) AS avg_salary_by_department
FROM employees
ORDER BY department, salary DESC;


-- Indexes
-- Indexes improve the speed of data retrieval by organizing the data in a specific way.
--  They help reduce the amount of data that needs to be scanned when performing queries.
CREATE INDEX idx_employees_department ON employees (department);
CREATE INDEX idx_sales_sale_date ON sales (sale_date);
-- note : index will also create overhead when we write into the table 
--  and it will slow down the write operations.

-- EXPLAIN ANALYZE -
-- EXPLAIN ANALYZE command provides an execution plan for a SQL query.
--  It helps you understand how the query will be executed,
--  which can be useful for optimization and debugging.
EXPLAIN ANALYZE SELECT * FROM sales;

EXPLAIN ANALYSE select emp_name,emp_id from employees where salary>400;

select now();

-- handling the range query 
SELECT emp_name, hire_date
FROM employees
WHERE hire_date BETWEEN '2015-01-01' AND '2020-12-31';

-- extractng year , month  or Day 
SELECT emp_name, EXTRACT(YEAR FROM hire_date) as hire_year, 
EXTRACT(MONTH FROM hire_date) as hire_month , extract(day from hire_date) as hire_day
from employees;


-- Date Arithmetic
-- Performing date arithmetic using the date_part() function.
--  The date_part() function takes two arguments: the part to extract (e.g., 'year', 'month', 'day') 
-- and the date value.
-- age() - diff between two dates 
SELECT emp_name, hire_date,
date_part('year', AGE(hire_date, CURRENT_DATE)) as years_of_service
FROM employees;

-- Date Formatting
-- Formatting dates using the to_char() function.
--  The to_char() function takes two arguments: the date value and the desired format.
SELECT emp_name, hire_date,
to_char(hire_date, 'DD-MM-YYYY : HH:MM') as hire_date_formatted


SELECT * from sales
where region IN ('West','East')


