package com.foodordering.controllers;

import com.foodordering.models.CartItem;
import com.foodordering.services.CartService;
import com.foodordering.database.DatabaseConnection;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class CartController {

    @FXML private ListView<HBox> cartListView;
    @FXML private Label totalAmountLabel;

    @FXML
    public void initialize() {
        refreshCartView();
    }

    private void refreshCartView() {
        cartListView.getItems().clear();

        if (CartService.isEmpty()) {
            cartListView.getItems().add(new HBox(new Label("Your cart is currently empty.")));
            totalAmountLabel.setText("Total: $0.00");
            return;
        }

        for (CartItem item : CartService.getItems()) {
            Label itemLabel = new Label(item.getDisplay());
            itemLabel.setPrefWidth(300);

            Button removeButton = new Button("Remove");
            removeButton.setStyle("-fx-background-color: #e74c3c; -fx-text-fill: white;");
            removeButton.setOnAction(e -> {
                CartService.removeItem(item);
                refreshCartView();
            });

            HBox row = new HBox(10, itemLabel, removeButton);
            row.setStyle("-fx-padding: 8; -fx-alignment: center-left;");
            cartListView.getItems().add(row);
        }

        totalAmountLabel.setText("Total: $" + String.format("%.2f", CartService.getTotalAmount()));
    }

    @FXML
    public void handleClearCart() {
        CartService.clearCart();
        refreshCartView();
    }

    @FXML
    public void handleCheckout() {
        if (CartService.isEmpty()) {
            showAlert("Cart is empty", "Please add items before checking out.");
            return;
        }

        try {
            Connection conn = DatabaseConnection.getInstance();

            // 1. Insert into Orders table
            PreparedStatement orderStmt = conn.prepareStatement(
                    "INSERT INTO Orders(user_id, total_amount, status) VALUES (?, ?, 'PLACED')",
                    PreparedStatement.RETURN_GENERATED_KEYS
            );
            orderStmt.setInt(1, 1); // TEMP: replace with actual user ID
            orderStmt.setDouble(2, CartService.getTotalAmount());
            orderStmt.executeUpdate();

            int orderId;
            try (ResultSet generatedKeys = orderStmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    orderId = generatedKeys.getInt(1);
                } else {
                    throw new IllegalStateException("Failed to retrieve order ID.");
                }
            }

            // 2. Insert items into OrderItems table
            PreparedStatement itemStmt = conn.prepareStatement(
                    "INSERT INTO OrderItems(order_id, item_name, item_price) VALUES (?, ?, ?)"
            );

            for (CartItem item : CartService.getItems()) {
                itemStmt.setInt(1, orderId);
                itemStmt.setString(2, item.getName());
                itemStmt.setDouble(3, item.getPrice());
                itemStmt.addBatch();
            }

            itemStmt.executeBatch();

            // 3. Show receipt modal
            showReceiptWindow();

            // 4. Clear and refresh cart
            CartService.clearCart();
            refreshCartView();

        } catch (Exception e) {
            e.printStackTrace();
            showAlert("Error", "Something went wrong while placing the order.");
        }
    }

    private void showReceiptWindow() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/views/Receipt.fxml"));
            Parent root = loader.load();

            Stage stage = new Stage();
            stage.setTitle("Order Receipt");
            stage.initModality(Modality.APPLICATION_MODAL);
            stage.setScene(new Scene(root));
            stage.showAndWait();
        } catch (Exception e) {
            e.printStackTrace();
            showAlert("Error", "Could not load receipt view.");
        }
    }

    @FXML
    public void handleClose() {
        Stage stage = (Stage) cartListView.getScene().getWindow();
        stage.close();
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION, message, ButtonType.OK);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.showAndWait();
    }
}
