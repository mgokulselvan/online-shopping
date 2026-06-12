SET SQLBLANKLINES ON /*setting so that blank spaces dont end the thing ,the query*/

CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) UNIQUE NOT NULL,
    phone VARCHAR2(20),
    password VARCHAR2(255) NOT NULL,
    address VARCHAR2(255)
);


CREATE TABLE products (
    product_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name VARCHAR2(150) NOT NULL,
    category VARCHAR2(100),
    price NUMBER(10,2) NOT NULL,
    stock_qty NUMBER DEFAULT 0 CHECK (stock_qty >= 0)
);

CREATE TABLE cart (
    cart_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id NUMBER NOT NULL,
    product_id NUMBER NOT NULL,

    quantity NUMBER DEFAULT 1 CHECK (quantity > 0),

    added_on DATE DEFAULT SYSDATE,

    CONSTRAINT fk_cart_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CONSTRAINT fk_cart_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE orders (
    order_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id NUMBER NOT NULL,

    order_date DATE DEFAULT SYSDATE,

    status VARCHAR2(30) DEFAULT 'PENDING',

    total_amount NUMBER(10,2) DEFAULT 0,

    CONSTRAINT fk_order_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);

CREATE TABLE order_items (
    order_item_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    order_id NUMBER NOT NULL,

    product_id NUMBER NOT NULL,

    quantity NUMBER NOT NULL CHECK (quantity > 0),

    price NUMBER(10,2) NOT NULL,

    CONSTRAINT fk_orderitem_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_orderitem_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    order_id NUMBER NOT NULL,

    payment_date DATE DEFAULT SYSDATE,

    amount NUMBER(10,2) NOT NULL,

    method VARCHAR2(50),

    status VARCHAR2(30) DEFAULT 'PENDING',

    CONSTRAINT fk_payment_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);


CREATE TABLE admins (
    admin_id NUMBER PRIMARY KEY,
    CONSTRAINT fk_admin_user
        FOREIGN KEY (admin_id)
        REFERENCES users(user_id)
);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Nike Crew Socks', 'Sports', 299, 50);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Adidas Ankle Socks', 'Sports', 249, 75);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Wool Winter Socks', 'Winter', 399, 30);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Cotton Everyday Socks', 'Casual', 199, 120);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Formal Black Socks', 'Formal', 179, 80);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Thermal Hiking Socks', 'Outdoor', 499, 25);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Striped Fashion Socks', 'Fashion', 229, 60);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Running Performance Socks', 'Sports', 349, 45);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Bamboo Comfort Socks', 'Eco', 279, 40);

INSERT INTO products (product_name, category, price, stock_qty)
VALUES ('Kids Cartoon Socks', 'Kids', 149, 100);

COMMIT;


INSERT INTO users(name,email,phone,password,address)
VALUES(
    'John Smith',
    'john@example.com',
    '1111111111',
    'john123',
    '123 Main Street'
);

INSERT INTO users(name,email,phone,password,address)
VALUES(
    'Sarah Johnson',
    'sarah@example.com',
    '2222222222',
    'sarah123',
    '456 Oak Avenue'
);

INSERT INTO users(name,email,phone,password,address)
VALUES(
    'Michael Brown',
    'michael@example.com',
    '3333333333',
    'michael123',
    '789 Pine Road'
);

INSERT INTO users(name,email,phone,password,address)
VALUES(
    'Emma Wilson',
    'emma@example.com',
    '4444444444',
    'emma123',
    '321 Cedar Lane'
);

COMMIT;

INSERT INTO admins(admin_id)
SELECT user_id
FROM users
WHERE email = 'john@example.com';

INSERT INTO admins(admin_id)
SELECT user_id
FROM users
WHERE email = 'sarah@example.com';

COMMIT;
