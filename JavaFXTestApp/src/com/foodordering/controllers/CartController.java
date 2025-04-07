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

public class CartController {

    @FXML private ListView<HBox> cartListView;
    @FXML private Label totalAmountLabel;

    @FXML
    public void initialize() {
        refreshCartView();
    }

    /**
     * Populates the ListView with cart items, each in its own HBox with a Remove button.
     */
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
            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO Orders(user_id, total_amount, status) VALUES (?, ?, 'PLACED')"
            );
            stmt.setInt(1, 1); // Replace with real user session if needed
            stmt.setDouble(2, CartService.getTotalAmount());
            stmt.executeUpdate();

            showReceiptWindow(); // ✅ Show receipt view
            CartService.clearCart(); // ✅ Clear cart after placing order
            refreshCartView(); // ✅ Refresh the UI

        } catch (Exception e) {
            e.printStackTrace();
            showAlert("Error", "Something went wrong while placing the order.");
        }
    }

    @FXML
    public void handleClose() {
        Stage stage = (Stage) cartListView.getScene().getWindow();
        stage.close();
    }

    /**
     * Opens the receipt screen in a modal window after successful checkout.
     */
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

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION, message, ButtonType.OK);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.showAndWait();
    }
}
