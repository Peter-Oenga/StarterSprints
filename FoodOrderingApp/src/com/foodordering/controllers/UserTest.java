package com.foodordering.controllers;

public class UserTest {
    public static void main(String[] args) {
        UserService service = new UserService();

        // Registration test (only once)
//         boolean registered = service.register("user123", "Passw0rd!", "CUSTOMER");
//        boolean c = service.register("new_user", "123456", "CUSTOMER");
//         System.out.println("Registration: " + c);

        // Login test
        String role = service.login("user123", "Passw0rd!");
        if (role != null) {
            System.out.println("Login successful. Role: " + role);
        } else {
            System.out.println("Login failed.");
        }
    }
}
