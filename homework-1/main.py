"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

with open("north_data/customers_data.csv", "r", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    current_row = 0
    for row in file_reader:
        if current_row != 0:
            print(len(row))
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        current_row += 1

with open("north_data/employees_data.csv", "r", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    current_row = 0
    for row in file_reader:
        if current_row != 0:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        current_row += 1

with open("north_data/orders_data.csv", "r", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    current_row = 0
    for row in file_reader:
        if current_row != 0:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
        current_row += 1

conn.commit()

cur.close()
conn.close()
