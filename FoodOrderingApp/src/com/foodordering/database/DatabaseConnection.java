package com.foodordering.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    private static Connection instance;

    private DatabaseConnection() {
        // Prevent direct instantiation
    }

    public static Connection getInstance() throws SQLException {
        if (instance == null || instance.isClosed()) {
            try {
                Class.forName("org.sqlite.JDBC"); // Optional but safe
                instance = DriverManager.getConnection("jdbc:sqlite:food_ordering.db");
                System.out.println("Connected to SQLite database.");
            } catch (ClassNotFoundException e) {
                System.err.println("SQLite JDBC driver not found.");
                throw new SQLException("Driver not found.", e);
            }
        }
        return instance;
    }
}
