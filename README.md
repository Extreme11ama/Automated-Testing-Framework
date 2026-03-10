# Automation Testing Framework

Automated UI testing framework built using Python, Playwright, and PyTest, 
following the Page Object Model design pattern.

## Test Coverage

### Login
- Successful login
- Locked out user error message

### Cart
- Add item to cart
- Remove item from cart

### Checkout
- Full checkout workflow
- Empty fields validation
- Checkout with empty cart

### Navigation
- Product sorting A-Z
- Logout functionality

## Features
- Page Object Model structure
- Screenshot capture on test failure
- HTML test reporting
- GitHub Actions CI/CD integration

## Tech Stack
- Python
- Playwright
- PyTest

## Test Target
https://www.saucedemo.com

## Setup
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Install browsers:
   playwright install
4. Run tests:
   pytest