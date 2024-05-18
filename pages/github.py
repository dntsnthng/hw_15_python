from selene import browser, have



class GithubPage:
    def open(self):
        browser.open('https://github.com/')
        return self

    def sd_login(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def mb_login(self):
        browser.element('.Button-label').click()
        browser.element('.HeaderMenu-link--sign-in').click()

    def page_have_text(self):
        browser.element('h1').should(have.text('Sign in to GitHub'))
