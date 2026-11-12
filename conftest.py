import pytest
import os
from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from datetime import datetime

@pytest.fixture

def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.navigate_to("https://www.saucedemo.com")
    return login

@pytest.fixture
def logged_in_inventory(page: Page) -> InventoryPage:
    login = LoginPage(page)
    login.navigate_to("https://www.saucedemo.com")
    login.login("standard_user", "secret_sauce")
    return InventoryPage(page)

def pytest_configure(config):
    """Konfig report HTML dan screenshoot"""
    if not os.path.exists("reports"):
        os.makedirs("reports")
        
    # Format nama file report berdasarkan tanggal & waktu
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    report_path = f"reports/report_{timestamp}.html"
    
    config.option.htmlpath = report_path
    config.option.self_contained_html = True
    config.option.screenshot = "only-on-failure"
    config.option.video = "only-on-failure"
           
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook untuk screenshot jika test gagal"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        
        if page:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            page.screenshot(path=f"{screenshot_dir}/{item.name}.png")
        
            pytest_html = item.config.pluginmanager.getplugin("html")
          
            if pytest_html:
                extra = getattr(report, "extra", [])
                screenshot_path = f"screenshots/{item.name}.png"
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra