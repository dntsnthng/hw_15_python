import pytest
from pages.github import GithubPage
from selene import browser


def test_github_desktop(browser_setup):
    if browser.config.window_width < 1000:
        pytest.skip('Standard tests for mobile')
    github_page = GithubPage()
    github_page.open()
    github_page.sd_login()
    github_page.page_have_text()


def test_github_mobile(browser_setup):
    if browser.config.window_width > 1000:
        pytest.skip('Tests for PC')
    github_page = GithubPage()
    github_page.open()
    github_page.mb_login()
    github_page.page_have_text()
