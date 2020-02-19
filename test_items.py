import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_have_add_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button is not False, "button adding to basket should be found on the page"
    time.sleep(3)
