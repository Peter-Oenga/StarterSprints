package com.foodordering.services;

import com.foodordering.models.CartItem;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CartService {

    private static final List<CartItem> cartItems = new ArrayList<>();

    // Adds a new item to the cart
    public static void addItem(String name, double price) {
        cartItems.add(new CartItem(name, price));
    }

    // Returns an unmodifiable list of cart items
    public static List<CartItem> getItems() {
        return Collections.unmodifiableList(cartItems);
    }

    // Removes a specific item (used for "Remove" button)
    public static void removeItem(CartItem item) {
        cartItems.remove(item);
    }

    // Clears the entire cart
    public static void clearCart() {
        cartItems.clear();
    }

    // Returns how many items are in the cart
    public static int getCartSize() {
        return cartItems.size();
    }

    // Checks if the cart is empty
    public static boolean isEmpty() {
        return cartItems.isEmpty();
    }

    // Returns the total amount of all items
    public static double getTotalAmount() {
        return cartItems.stream()
                .mapToDouble(CartItem::getPrice)
                .sum();
    }
}
