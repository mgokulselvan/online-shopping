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
    admin_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR2(50) UNIQUE,
    password VARCHAR2(255)
);
