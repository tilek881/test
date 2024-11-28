-- Создание таблицы categories
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY, -- Код категории (например, 'FD', 'EL', 'CL')
    title VARCHAR(150) NOT NULL -- Название категории (например, 'Food products')
);

-- Создание таблицы products
CREATE TABLE products (
    id INTEGER PRIMARY KEY, -- Уникальный идентификатор продукта
    title VARCHAR(250) NOT NULL, -- Название продукта
    category_code VARCHAR(2) NOT NULL, -- Код категории, внешний ключ
    unit_price FLOAT NOT NULL, -- Цена за единицу
    stock_quantity INTEGER NOT NULL, -- Количество на складе
    store_id INTEGER NOT NULL, -- Идентификатор магазина
    FOREIGN KEY (category_code) REFERENCES categories(code) -- Внешний ключ на таблицу categories
);

-- Пример для таблицы store
-- Поскольку информация о структуре таблицы store на картинке отсутствует, ниже базовый пример
CREATE TABLE store (
    id INTEGER PRIMARY KEY, -- Уникальный идентификатор магазина
    name VARCHAR(150) NOT NULL, -- Название магазина
    location VARCHAR(250) -- Местоположение магазина
);
