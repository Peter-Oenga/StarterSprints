package com.foodordering.controllers;

import com.foodordering.models.CartItem;
import com.foodordering.services.CartService;
import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ReceiptController {

    @FXML private TextArea receiptText;

    @FXML
    public void initialize() {
        StringBuilder receipt = new StringBuilder();

        receipt.append("🧾 Foodie's Paradise - Order Receipt\n\n");
        receipt.append("Date: ")
                .append(LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")))
                .append("\n\n");

        for (CartItem item : CartService.getItems()) {
            receipt.append("• ").append(item.getDisplay()).append("\n");
        }

        receipt.append("\n-------------------------\n");
        receipt.append("Total: $").append(String.format("%.2f", CartService.getTotalAmount()));
        receipt.append("\n\nThank you for your order!");

        receiptText.setText(receipt.toString());
    }

    @FXML
    public void handleClose() {
        Stage stage = (Stage) receiptText.getScene().getWindow();
        stage.close();
    }
}
