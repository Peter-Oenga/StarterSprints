package com.foodordering.controllers;

import com.foodordering.database.DatabaseConnection;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class UserDashboardController {

    @FXML private ComboBox<String> itemComboBox;
    @FXML private TextField amountField;
    @FXML private Label statusLabel;

    /**
     * Initializes the controller by pre-populating menu items.
     */
    @FXML
    public void initialize() {
        itemComboBox.getItems().addAll(
                "🍔 Burger",
                "🍕 Pizza",
                "🍣 Sushi",
                "🥗 Salad",
                "🍗 Fried Chicken",
                "🍟 Fries",
                "🥞 Pancakes",
                "🍜 Noodles",
                "🥪 Sandwich"
        );
        itemComboBox.setValue("🍔 Burger"); // Default selection
    }

    @FXML
    public void handlePlaceOrder() {
        String item = itemComboBox.getValue();
        String amountText = amountField.getText();

        try {
            double amount = Double.parseDouble(amountText);
            if (amount <= 0) {
                statusLabel.setText("Amount must be greater than 0.");
                return;
            }

            // Remove emoji for DB entry (optional but cleaner)
            String itemClean = item.replaceAll("^[^a-zA-Z]+\\s*", "");

            Connection conn = DatabaseConnection.getInstance();
            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO Orders(user_id, total_amount, status) VALUES (?, ?, 'PENDING')"
            );
            stmt.setInt(1, 1); // TEMP: hardcoded user_id
            stmt.setDouble(2, amount);
            stmt.executeUpdate();

            statusLabel.setText("Order for " + itemClean + " placed successfully!");

        } catch (NumberFormatException e) {
            statusLabel.setText("Invalid amount.");
        } catch (Exception e) {
            e.printStackTrace();
            statusLabel.setText("Error placing order.");
        }
    }
}
