package com.foodordering.controllers;

import com.foodordering.database.DatabaseConnection;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

import java.io.FileWriter;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class AdminDashboardController {

    @FXML private Label reportStatusLabel;

    @FXML
    public void handleGenerateReport() {
        try {
            Connection conn = DatabaseConnection.getInstance();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT order_id, total_amount, status FROM Orders");

            FileWriter writer = new FileWriter("sales_report.csv");
            writer.write("Order ID,Amount,Status\n");

            while (rs.next()) {
                writer.write(
                        rs.getInt("order_id") + "," +
                                rs.getDouble("total_amount") + "," +
                                rs.getString("status") + "\n"
                );
            }

            writer.close();
            reportStatusLabel.setText("Report generated: sales_report.csv");
        } catch (Exception e) {
            e.printStackTrace();
            reportStatusLabel.setText("Failed to generate report.");
        }
    }
}
