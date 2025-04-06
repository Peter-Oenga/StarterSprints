package com.foodordering.controllers;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

public class LoginController {

    @FXML private TextField usernameField;
    @FXML private PasswordField passwordField;
    @FXML private Label errorLabel;

    private final UserService userService = new UserService();

    @FXML
    public void handleLogin() {
        String username = usernameField.getText().trim();
        String password = passwordField.getText();

        errorLabel.setText(""); // Clear any previous errors

        if (username.isEmpty() || password.isEmpty()) {
            errorLabel.setText("Please fill in all fields.");
            return;
        }

        String role = userService.login(username, password);

        if (role != null) {
            try {
                String viewPath = switch (role) {
                    case "RESTAURANT_ADMIN" -> "/views/AdminDashboard.fxml";
                    default -> "/views/UserDashboard.fxml";
                };
                Parent root = FXMLLoader.load(getClass().getResource(viewPath));
                Stage stage = (Stage) usernameField.getScene().getWindow();
                stage.setScene(new Scene(root));
            } catch (Exception e) {
                errorLabel.setText("Failed to load dashboard.");
                e.printStackTrace();
            }
        } else {
            errorLabel.setText("Invalid username or password.");
        }
    }
}
