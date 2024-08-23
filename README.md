# Selenium Web Testing
A comprehensive Selenium WebDriver test suite for the Sauce Demo website, covering key functionalities including user authentication and checkout processes. Integrated with GitHub Actions for manual test execution. Includes detailed documentation and setup instructions.

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
   - Install `pip-tools`: `pip install pip-tools`
   - **Compile dependencies**:
     - The `requirements.in` file lists your project's top-level dependencies.
     - To generate a `requirements.txt` file that includes all transitive dependencies, run: `pip-compile requirements.in`
     - This command will create or update the `requirements.txt` file.
     - Use `pip-sync` to install the dependencies listed in `requirements.txt`: `pip-sync`
     - `pip-sync` automatically installs and uninstalls packages based on the packages mentioned in `requirements.in`.

2. **Run Tests:**
   - Execute tests with Pytest: `pytest`
   - Run a specific test file: `pytest tests/test_user_authentication.py`
   - Generate an HTML report: `pytest --html=reports/test_report.html --self-contained-html`

## GitHub Actions

The test suite is integrated with GitHub Actions. Tests are automatically executed on push or manually triggered from the Actions tab.
