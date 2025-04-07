package com.foodordering.database;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.Statement;

public class DatabaseInitializer {
    public static void main(String[] args) {
        try {
            Connection conn = DatabaseConnection.getInstance();
            String sql = Files.readString(Paths.get("init.sql")); // Make sure path is correct
            Statement stmt = conn.createStatement();
            stmt.executeUpdate(sql);
            System.out.println("Database initialized successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
