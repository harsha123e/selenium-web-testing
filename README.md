# Selenium Web Testing
A comprehensive Selenium WebDriver test suite for the Sauce Demo website, covering key functionalities including user authentication and checkout processes. Integrated with GitHub Actions for manual test execution. Includes detailed documentation and setup instructions.

# [Sauce Demo](https://www.saucedemo.com/) Automated Testing Suite

## Test Cases

1. **User Authentication**
   - Verify login with valid credentials.
   - Verify login with invalid credentials.
   - Verify logout functionality.

2. **Product Interaction**
   - Test product search functionality.
   - Test product selection and addition to the cart.

3. **Shopping Cart Management**
   - Test adding multiple products to the cart.
   - Test updating product quantities in the cart.
   - Test removing products from the cart.

4. **Checkout Process**
   - Test completing a purchase with valid information.
   - Verify order confirmation.

## Setup

1. **Install Dependencies:**
   - Create a virtual environment: `python -m venv venv`
   - Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
   - Install requirements: `pip install -r requirements.txt`

2. **Run Tests:**
   - Execute tests: `python -m unittest discover -s tests`

## GitHub Actions

The test suite is integrated with GitHub Actions. Tests are automatically executed on push or manually triggered from the Actions tab.