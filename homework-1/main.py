import csv

import psycopg2


def main():
    with open(r'north_data/customers_data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        customer_tuples = [tuple(i) for i in reader][1:]
    with open(r'north_data/orders_data.csv', encoding='utf-8') as f:
        order_tuples = [tuple(i) for i in csv.reader(f)][1:]
    with open(r'north_data/employees_data.csv', encoding='utf-8') as f:
        employee_tuples = [tuple(i) for i in csv.reader(f)][1:]
        print(employee_tuples)

    conn = psycopg2.connect(host='localhost',
                            database='north',
                            user='postgres',
                            password='12345')

    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employee_tuples)
                cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customer_tuples)
                cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', order_tuples)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
