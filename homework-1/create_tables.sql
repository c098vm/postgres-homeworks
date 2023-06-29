-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id smallint PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(40) NOT NULL,
	contact_name varchar(40) NOT NULL
);

CREATE TABLE orders
(
	order_id smallint PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id smallint REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
);