package com.foodordering.database;

import java.sql.Connection;
import java.sql.SQLException;

public class DatabaseTest {
    public static void main(String[] args) {
        try {
            Connection conn = DatabaseConnection.getInstance();
            if (conn != null) {
                System.out.println("Database connection successful.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
