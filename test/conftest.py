import pytest
import os

from selene import browser



@pytest.fixture
def standard_browser(request):
    browser.config.window_width = os.getenv('window_width', '1900')
    browser.config.window_height = os.getenv('window_height', '1400')
    yield browser
    browser.quit()

@pytest.fixture
def mobile_browser():
    browser.config.window_width = os.getenv('window_width', '400')
    browser.config.window_height = os.getenv('window_height', '800')
    yield browser
    browser.quit()

@pytest.fixture(params=['standard', 'mobile'])
def browser_sd(request):
    if request.param == 'standard':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 400
        browser.config.window_height = 800
    yield
    browser.quit()

@pytest.fixture(params=[(1920, 1080), (400, 800)])
def browser_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

