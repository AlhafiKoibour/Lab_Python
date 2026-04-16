CREATE DATABASE employees_db;

\c employees_db;

CREATE TABLE employees (
    emp_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    position VARCHAR(50),
    salary FLOAT
);