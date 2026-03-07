import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs["page"]
        page.screenshot(path="failure.png")
