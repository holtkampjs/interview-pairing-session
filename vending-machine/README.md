# Vending Machine

## Basic Requirements

1. Product Inventory:
  The vending machine should have a list of products, each with a name, price, and quantity.
  Provide functions to add, remove, or modify products.
1. Insert Coins:
  Allow users to insert coins (e.g., pennies, nickels, dimes, quarters, etc.).
  Keep track of the total amount inserted.
  Return an error if a non-accepted coin is inserted.
1. Purchase Product:
  Allow users to select a product.
  Check if enough money has been inserted.
  Deduct the product price from the total amount inserted and update the product’s quantity.
  Return an error if the product is out of stock or if not enough money has been inserted.
1. Return Change:
  If a purchase is successful and there’s a remaining balance, return the balance to the user in the least number of coins possible.
  If the machine doesn’t have enough change, prevent the purchase and inform the user.
1. Dispense Product:
  Once a purchase is successful, dispense the selected product.

## Intermediate Requirements

1. Coin Inventory:
  Track the number of each coin the vending machine has for giving change.
  Provide functions to add or remove coins from the inventory.
1. Product Dispense History:
  Keep a history of dispensed products with timestamps.
1. Cancel Transaction:
  Allow users to cancel a transaction and get back the inserted coins.

## Advanced Requirements

1. Multiple Product Selection:
  Allow users to select multiple products in a single transaction.
1. Special Offers:
  Implement special offers like “Buy 1 Get 1 Free” or discounts.
1. Admin Functions:
  Provide password-protected admin functions to:View sales reports.
  Refill products.
  Refill coins.
  Change product prices.
1. Error Handling and Notifications:
  Inform users if the machine is out of service.
  Notify the admin if the machine is running low on products or coins.
