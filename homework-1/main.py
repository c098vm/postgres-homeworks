"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def csvtodb(filename):
    """
    Функция считывает данные из файла и записывает в таблицу базы данных
    """

    # Открываем файл для чтения и подгружаем csv-данные
    file = open(f"north_data/{filename}", "r", encoding='utf-8')
    csv_data = csv.reader(file, delimiter=",")

    # Создаем соединение с базой данных
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    current_row = 0
    column_count = 0

    # Определяем имя таблица по имени файла
    table = filename[0:-9]

    # Итерируем объект с csv-данными построчно и через SQL-команду
    # записываем значения в очередную строкук таблицы
    for row in csv_data:
        if current_row == 0:
            column_count = len(row)
        else:
            place_holders_string = (column_count * "%s, ")[0:-2]
            cur.execute(f"INSERT INTO {table} VALUES ({place_holders_string})", row)
        current_row += 1

    conn.commit()
    cur.close()
    conn.close()
    file.close()


csvtodb("customers_data.csv")
csvtodb("employees_data.csv")
csvtodb("orders_data.csv")
