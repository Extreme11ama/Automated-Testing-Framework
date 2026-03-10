## Bug #1 – Checkout form allows submission with empty cart

**Environment:**
- Browser: Chrome (latest)
- OS: Windows 11
- Test URL: https://www.saucedemo.com

**Steps to Reproduce:**
1. Login with valid credentials
2. Click cart icon
3. Click checkout with no items in cart
4. Fill in valid checkout details
5. Click continue
6. Click finish

**Expected Result:**
User should be prevented from checking out with an empty cart,
or shown a warning message.

**Actual Result:**
Checkout process completes successfully with an empty cart,
no error or warning is shown.

**Severity:** Medium

**Priority:** Low

**Status:** Open