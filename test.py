import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE store (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);
""")

# Заполнение тестовыми данными
cursor.executemany("INSERT INTO categories (code, title) VALUES (?, ?);", [
    ('FD', 'Food products'),
    ('EL', 'Electronics'),
    ('CL', 'Clothes')
])

cursor.executemany("INSERT INTO store (store_id, title) VALUES (?, ?);", [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar')
])

cursor.executemany("""
INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id)
VALUES (?, ?, ?, ?, ?, ?);
""", [
    (1, 'Chocolate', 'FD', 10.5, 129, 1),
    (2, 'Jeans', 'CL', 120.0, 15, 2),
    (3, 'T-Shirt', 'CL', 20.0, 10, 3)
])

connection.commit()


# Программа
def main():
    while True:
        print(
            "\nВы можете отобразить список продуктов по выбранному id магазина из перечня ниже, для выхода из программы введите цифру 0:\n")

        # Вывод списка магазинов
        cursor.execute("SELECT store_id, title FROM store;")
        stores = cursor.fetchall()
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        # Ввод пользователя
        try:
            user_input = int(input("\nВведите id магазина (или 0 для выхода): "))
        except ValueError:
            print("Пожалуйста, введите корректное число!")
            continue

        if user_input == 0:
            print("Выход из программы...")
            break

        # Проверка наличия магазина
        cursor.execute("SELECT title FROM store WHERE store_id = ?;", (user_input,))
        store = cursor.fetchone()
        if not store:
            print("Магазин с таким id не найден, попробуйте снова.")
            continue

        # Вывод продуктов для выбранного магазина
        print(f"\nТовары в магазине '{store[0]}':")
        cursor.execute("""
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?;
        """, (user_input,))
        products = cursor.fetchall()

        if not products:
            print("В данном магазине нет доступных товаров.")
        else:
            for product in products:
                print(
                    f"Название продукта: {product[0]}\nКатегория: {product[1]}\nЦена: {product[2]}\nКоличество на складе: {product[3]}\n")


if __name__ == "__main__":
    main()

# Закрытие соединения
connection.close()


