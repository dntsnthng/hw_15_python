from pages.github import GithubPage




def test_mobile_gh(mobile_browser):
    github_page = GithubPage()
    github_page.open()
    github_page.mb_login()
    github_page.page_have_text()



def test_standard_gh(standard_browser):
    github_page = GithubPage()
    github_page.open()
    github_page.sd_login()
    github_page.page_have_text()





