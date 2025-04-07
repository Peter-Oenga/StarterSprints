package com.foodordering.models;

/**
 * Represents a single item in the shopping cart.
 */
public class CartItem {
    private final String name;
    private final double price;

    public CartItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    /**
     * Returns the item name, e.g., "Burger".
     */
    public String getName() {
        return name;
    }

    /**
     * Returns the item price, e.g., 5.99.
     */
    public double getPrice() {
        return price;
    }

    /**
     * Returns a display-friendly version for the UI,
     * e.g., "Burger - $5.99".
     */
    public String getDisplay() {
        return name + " - $" + String.format("%.2f", price);
    }

    /**
     * Optional: Overrides toString so it’s clean when debugging or printing.
     */
    @Override
    public String toString() {
        return getDisplay();
    }

    /**
     * Optional: Define equals() and hashCode() if you want to support remove by object.
     * This helps when removing items from List<CartItem>.
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof CartItem)) return false;
        CartItem item = (CartItem) o;
        return Double.compare(item.price, price) == 0 && name.equals(item.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode() + Double.hashCode(price);
    }
}
