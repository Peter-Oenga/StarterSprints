package com.foodordering.controllers;

import com.foodordering.database.DatabaseConnection;

import java.security.MessageDigest;
import java.sql.*;

public class UserService {

    public boolean register(String username, String password, String role) {
        try {
            Connection conn = DatabaseConnection.getInstance();
            String hashedPassword = hashPassword(password);
            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO Users(username, password_hash, role) VALUES (?, ?, ?)");
            stmt.setString(1, username);
            stmt.setString(2, hashedPassword);
            stmt.setString(3, role);
            stmt.executeUpdate();
            return true;
        } catch (SQLException e) {
            System.out.println("Registration failed: " + e.getMessage());
            return false;
        }
    }

    public String login(String username, String password) {
        try {
            Connection conn = DatabaseConnection.getInstance();
            String hashedPassword = hashPassword(password);
            PreparedStatement stmt = conn.prepareStatement(
                    "SELECT role FROM Users WHERE username = ? AND password_hash = ?");
            stmt.setString(1, username);
            stmt.setString(2, hashedPassword);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return rs.getString("role"); // Login success, return role
            } else {
                return null; // Login failed
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : hash) sb.append(String.format("%02x", b));
            return sb.toString();
        } catch (Exception e) {
            throw new RuntimeException("Hashing error");
        }
    }
}
