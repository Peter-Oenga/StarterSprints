package com.foodordering.controllers;

import com.foodordering.models.CartItem;
import com.foodordering.services.CartService;
import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ReceiptController {

    @FXML
    private TextArea receiptText;

    @FXML
    public void initialize() {
        StringBuilder receipt = new StringBuilder();

        // Header
        receipt.append("        🧾 Foodie's Paradise\n");
        receipt.append("      ---------------------------\n\n");

        // Timestamp
        String date = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        receipt.append("Date: ").append(date).append("\n\n");

        // Items
        if (CartService.isEmpty()) {
            receipt.append("Your cart was empty.\n");
        } else {
            receipt.append("Items:\n");
            for (CartItem item : CartService.getItems()) {
                receipt.append("• ").append(item.getDisplay()).append("\n");
            }
        }

        // Divider & total
        receipt.append("\n---------------------------\n");
        receipt.append("Total: $").append(String.format("%.2f", CartService.getTotalAmount())).append("\n");
        receipt.append("---------------------------\n");

        // Footer
        receipt.append("\nThank you for ordering with us!\n");
        receipt.append("Enjoy your meal 🍽️");

        receiptText.setText(receipt.toString());
    }

    @FXML
    public void handleClose() {
        Stage stage = (Stage) receiptText.getScene().getWindow();
        stage.close();
    }
}
