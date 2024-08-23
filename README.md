# Selenium Web Testing
The Selenium Web Testing suite is designed to automate the testing of the Sauce Demo website. This project aims to ensure that key functionalities such as user authentication, product interaction, and checkout processes work as expected. The tests are integrated with GitHub Actions to enable continuous integration and manual execution.

### Technologies Used

- **Selenium WebDriver**: For browser automation.
- **Python**: Programming language used for writing test scripts.
- **pytest**: Framework for running tests and generating reports.
- **Docker and GitHub Actions**: For CI/CD pipeline and automated test execution.

# [Sauce Demo](https://www.saucedemo.com/) Automated Testing Suite

## Test Cases

1. **User Authentication**
   - Verify login with valid credentials.
   - Verify login with invalid credentials.
   - Verify logout functionality.

2. **Product Interaction**
   - Test product selection and addition to the cart.

3. **Shopping Cart Management**
   - Test adding multiple products to the cart.
   - Test removing products from the cart.

4. **Checkout Process**
   - Test completing a purchase with valid information.

## Setup

1. **Install Dependencies:**
   - Create a virtual environment: `python -m venv venv`
   - Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
   - Install **pip-tools**: `pip install pip-tools`
   - **Compile dependencies**:
     - The *requirements.in* file lists your project's top-level dependencies.
     - To generate a *requirements.txt* file that includes all transitive dependencies, run: `pip-compile requirements.in`
     - This command will create or update the *requirements.txt* file.
     - Use **pip-sync** to install the dependencies listed in *requirements.txt*: `pip-sync`
     - **pip-sync** automatically installs and uninstalls packages based on the packages mentioned in *requirements.in*.

2. **Run Tests:**
   - Execute tests with Pytest: `pytest`
   - Run a specific test file: `pytest tests/test_user_authentication.py`
   - Generate an HTML report: `pytest --html=reports/test_report.html --self-contained-html`

## GitHub Actions

The test suite is integrated with GitHub Actions. Tests are automatically executed on push or manually triggered from the Actions tab. Reports are generated on successful test execution.

## Test Report

Generated using pytest-html

![image](https://github.com/user-attachments/assets/e58a1212-6b9b-41ec-a190-5dd4efcad974)


## Test Case Steps

These test cases are automated using Selenium

### Test Case 1: User Login

**Objective**: Verify user login functionality with both valid and invalid credentials.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type the specified `username` into the username field.
3. **Enter Password**: Type the specified `password` into the password field.
4. **Click Login Button**: Click on the login button.
5. **Verify Outcome**:
   - If using valid credentials (`standard_user`):
     - **Check Welcome Message**: Ensure that the welcome message matches 'Products'.
   - If using invalid credentials:
     - **Check Error Message**: Ensure the error message contains 'Epic sadface:'.

### Test Case 2: User Logout

**Objective**: Verify that a user can log out successfully.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type 'standard_user' into the username field.
3. **Enter Password**: Type 'secret_sauce' into the password field.
4. **Click Login Button**: Click on the login button.
5. **Open Menu**: Click on the menu button (three horizontal lines).
6. **Click Logout**: Click on the logout link.
7. **Verify Logout**: Ensure the login button is displayed on the login page.

### Test Case 3: Product Selection and Addition to Cart

**Objective**: Verify that a product can be selected and added to the shopping cart.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type 'standard_user' into the username field.
3. **Enter Password**: Type 'secret_sauce' into the password field.
4. **Click Login Button**: Click on the login button.
5. **Select Product**: Choose the first product from the list.
6. **Add Product to Cart**: Click on the 'Add to Cart' button for the selected product.
7. **Verify Cart Badge**: Ensure that the shopping cart badge displays '1', indicating the product was added to the cart.

### Test Case 4: Complete Purchase

**Objective**: Verify that a user can complete a purchase successfully.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type 'standard_user' into the username field.
3. **Enter Password**: Type 'secret_sauce' into the password field.
4. **Click Login Button**: Click on the login button.
5. **Select Product**: Choose a product and add it to the cart.
6. **Open Cart**: Click on the shopping cart link.
7. **Proceed to Checkout**: Click on the checkout button.
8. **Enter Shipping Information**: Fill in the first name, last name, and postal code fields.
9. **Continue Checkout**: Click on the continue button.
10. **Complete Purchase**: Click on the finish button.
11. **Verify Confirmation**: Ensure the confirmation message contains "thank you for your order".

### Test Case 5: Adding Multiple Products to Cart

**Objective**: Verify that multiple products can be added to the cart.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type 'standard_user' into the username field.
3. **Enter Password**: Type 'secret_sauce' into the password field.
4. **Click Login Button**: Click on the login button.
5. **Add All Products to Cart**: Click 'Add to Cart' for each product listed.
6. **Verify Cart Badge**: Ensure the shopping cart badge displays the total number of products added.

### Test Case 6: Removing Products from Cart

**Objective**: Verify that a product can be removed from the cart.

**Steps**:
1. **Navigate to Sauce Demo Login Page**: Open `https://www.saucedemo.com`.
2. **Enter Username**: Type 'standard_user' into the username field.
3. **Enter Password**: Type 'secret_sauce' into the password field.
4. **Click Login Button**: Click on the login button.
5. **Add Product to Cart**: Click 'Add to Cart' for one product.
6. **Open Cart**: Click on the shopping cart link.
7. **Capture Initial Cart Count**: Note the number of items in the cart.
8. **Remove Product from Cart**: Click on the remove button for the product.
9. **Verify Cart Count**: Ensure the number of items in the cart has decreased by one.

## Acknowledgements

Thanks to the creators of Selenium WebDriver, pytest, and GitHub Actions for their fantastic tools that make automated testing and continuous integration so accessible.
