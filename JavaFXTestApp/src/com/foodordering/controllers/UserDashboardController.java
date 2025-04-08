package com.foodordering.controllers;

import com.foodordering.database.DatabaseConnection;
import com.foodordering.models.CartItem;
import com.foodordering.services.CartService;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class UserDashboardController {

    @FXML private ComboBox<String> itemComboBox;
    @FXML private TextField amountField;
    @FXML private Label statusLabel;
    @FXML private Label cartStatusLabel;
    @FXML private Label cartSummaryLabel;

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
        itemComboBox.setValue("🍔 Burger");

        // Initial cart label
        cartStatusLabel.setText("Cart: " + CartService.getCartSize() + " items");
    }

    @FXML
    public void handleViewCart() {
        if (CartService.isEmpty()) {
            cartSummaryLabel.setText("🛒 Your cart is empty.");
            return;
        }

        StringBuilder summary = new StringBuilder("🧾 Cart Summary:\n\n");
        for (CartItem item : CartService.getItems()) {
            summary.append("• ").append(item.getDisplay()).append("\n");
        }

        summary.append("\n💰 Total: $").append(String.format("%.2f", CartService.getTotalAmount()));
        cartSummaryLabel.setText(summary.toString());
    }

    @FXML
    public void openCartModal() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/views/Cart.fxml"));
            Parent root = loader.load();

            Stage cartStage = new Stage();
            cartStage.setTitle("Your Cart");
            cartStage.initModality(Modality.APPLICATION_MODAL);
            cartStage.setScene(new Scene(root));
            cartStage.showAndWait();
        } catch (Exception e) {
            e.printStackTrace();
        }
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

    @FXML
    public void handleFoodClick(MouseEvent event) {
        VBox clickedCard = (VBox) event.getSource();
        Label label = (Label) clickedCard.getChildren().get(1);
        String itemText = label.getText();

        itemComboBox.setValue(itemText);
        System.out.println("You clicked on: " + itemText);
    }

    @FXML
    public void handleAddToCart(ActionEvent event) {
        Button button = (Button) event.getSource();
        VBox parent = (VBox) button.getParent();
        Label label = (Label) parent.getChildren().get(1); // e.g. "Burger - $5.99"

        try {
            String[] parts = label.getText().split(" - \\$");
            String name = parts[0].trim();
            double price = Double.parseDouble(parts[1].trim());

            CartService.addItem(name, price);

            cartStatusLabel.setText("Cart: " + CartService.getCartSize() + " items");
            statusLabel.setText(name + " added to cart.");

            handleViewCart();

        } catch (Exception e) {
            statusLabel.setText("Failed to add to cart.");
            e.printStackTrace();
        }
    }
}
