from selene import browser, be, have


def test_search_positive(browser_settings):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_negative(browser_settings):
    browser.element('[name="q"]').should(be.blank).type('sta12223sssshdhdggubo').press_enter()
    browser.element('[id="main"]').should(have.text('did not match any documents'))
