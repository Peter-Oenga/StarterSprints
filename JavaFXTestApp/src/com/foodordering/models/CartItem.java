package com.foodordering.models;

public class CartItem {
    private final String name;
    private final double price;

    public CartItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getDisplay() {
        return name + " - $" + String.format("%.2f", price);
    }

    public String getName() { return name; }
    public double getPrice() { return price; }
}
