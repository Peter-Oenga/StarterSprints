CREATE TABLE IF NOT EXISTS Users (
                                     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     username TEXT UNIQUE NOT NULL,
                                     password_hash TEXT NOT NULL,
                                     role TEXT CHECK(role IN ('CUSTOMER', 'RESTAURANT_ADMIN', 'SYSTEM_ADMIN')) NOT NULL
    );

CREATE TABLE IF NOT EXISTS Orders (
                                      order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      user_id INTEGER,
                                      total_amount REAL,
                                      status TEXT CHECK(status IN ('PENDING', 'PAID', 'CANCELLED')),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
