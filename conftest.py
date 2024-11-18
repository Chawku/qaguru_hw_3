import pytest
from selene import browser


@pytest.fixture()
def browser_settings():
    browser.open('https://www.google.com/ncr')
    browser.driver.set_window_size(1920, 1080)
    browser.config.timeout = 10
    yield
    browser.quit()
