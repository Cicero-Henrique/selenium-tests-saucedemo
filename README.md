# Selenium Tests on saucedemo

This is a repo just to improve my skills using Selenium with Pytest on [Saucedemo](https://www.saucedemo.com/v1/index.html)

## Test Execution Plan

| ID | Page | Title | Preconditions | Steps | Expected Results | Status |
| -- | ---- | ----- | ------------- | ----- | ---------------- | ------ |
| TC-01 | Login | Successful login | User is on the login page | 1. Enter a valid username. <br/> 2. Enter a valid password. <br/> 3. Click the login button. | 1. Login is successful. <br/> 2. The user is redirected to the inventory page. | PASS |
| TC-02 | Login | Invalid user | User is on the login page | 1. Enter an invalid username and password. <br/> 2. Click the login button. | 1. The login is not successful. <br/> 2. Error message alerts users that they are not registered. | PASS |
| TC-03 | Login | Empty username | User is on the login page | 1. Do not enter a username. <br/> 2. Enter a password. <br/> 3. Click the login button. | 1. The login is not successful. <br/> 2. Error message alerts the user that the username field is missing. | PASS |
| TC-04 | Login | Empty password | User is on the login page | 1. Enter a username. <br/> 2. Do not enter a password. <br/> 3. Click the login button. | 1. The login is not successful. <br/> 2. Error message alerts the user that the password field is missing. | PASS |
| TC-05 | Inventory | All items button | User is on the cart page | 1. Click the side menu. <br/> 2. Click the "All items" button. | User is redirected to the inventory page. | PASS |
| TC-06 | Inventory | About button | N/A | 1. Click the side menu. <br/> 2. Click the "About" button. | User is redirected to the soucelabs page. | PASS |
| TC-07 | Inventory | Logout button | N/A | 1. Click the side menu. <br/> 2. Click the "Logout" button. | 1. The user is logged out successfully. <br/> 2. The user is redirected to the login page. | PASS |
| TC-08 | Inventory | Reset App State button | N/A | 1. Add the first product to the cart. <br/> 2. Verify that "1" is added to the cart icon. <br/> 3. Click the side menu. <br/> 4. Click the "Reset App State" button. | The cart should be empty. | PASS |
| TC-09 | Inventory | Sort A to Z | N/A | 1. Select the "Name (A to Z)" option in the dropdown. | Products should be sorted alphabetically. | PASS |
| TC-10 | Inventory | Sort Z to A | N/A | 1. Select the "Name (Z to A)" option in the dropdown. | Products should be sorted in reverse alphabetical order. | PASS |
| TC-11 | Inventory | Sort by ascending price | N/A | 1. Select the "Price (low to high)" in the dropdown. | Products should be sorted from the cheapest to the most expensive. | PASS |
| TC-12 | Inventory | Sort by descending price | N/A | 1. Select the "Price (high to low)" in the dropdown. | Products should be sorted from the most expensive to the cheapest. | PASS |
| TC-13 | Inventory | Add products to cart | N/A | 1. Click the "Add to cart" button on two products. <br/> 2. Access the cart. | 1. Both products should be in the cart page. <br/> 2. The cart icon counter should display 2. | PASS |
| TC-14 | Product Page | Verify product name | N/A | 1. Access the product page. | The product name in the inventory should match the one on the product page. | PASS |
| TC-15 | Product Page | Verify product description | N/A | 1. Access the product page. | The product description in the inventory should match the one on the product page. | PASS |
| TC-16 | Product Page | Verify product price | N/A | 1. Access the product page. | The product price in the inventory should match the one on the product page. | PASS |
| TC-17 | Product Page | Return to inventory | N/A | 1. Access the product page. <br/> 2. Click the "Back" button. | The user should be redirected to the inventory. | PASS |
| TC-18 | Product Page | Add to cart from product page | N/A | 1. Access the product page. <br/> 2. Click the "Add to cart" button. | The cart icon counter should display 1. | PASS |
| TC-19 | Cart | Remove products from cart | N/A | 1. Add two products to the cart. <br/> 2. Remove one product. | 1. The product should be removed from the cart. <br/> 2. The icon should indicate 1. | PASS |
| TC-20 | Checkout | Verify checkout information | User must have at least one product added to the cart | 1. Complete the checkout form. <br/> 2. Access the checkout page. | The product name, price, and description should match those from the inventory. | PASS |
| TC-21 | Checkout | Complete purchase | User must have at least one product added to the cart | 1. Access the checkout page with products added. <br/> 2. Click the "Finish" button. | User should be redirected to the "checkout complete" page. | PASS |
| TC-22 | Product Page | Add invalid product to cart | N/A | 1. Access the invalid product page. <br/> 2. Try to add it to the cart. | The product should not be added to the cart. | FAIL |
| TC-23 | Inventory | Product buttons after reset | N/A | 1. Add a product to the cart. <br/> 2. Click the "Reset App State" button. | The button text for the added product should be "Add to cart". | FAIL |
