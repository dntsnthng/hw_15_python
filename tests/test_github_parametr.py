import pytest
from pages.github import GithubPage


@pytest.mark.parametrize('browser_sd', ['standard'], indirect=True)
def test_browser_pc(browser_sd):
    github_page = GithubPage()
    github_page.open()
    github_page.sd_login()
    github_page.page_have_text()


@pytest.mark.parametrize('browser_sd', ['mobile'], indirect=True)
def test_browser_mb(browser_sd):
    github_page = GithubPage()
    github_page.open()
    github_page.mb_login()
    github_page.page_have_text()
