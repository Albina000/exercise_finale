from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class PageObjectLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ELEMENT_TEXT_KORZ = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")
    ELEMENT_TEXT_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_KORZ = (By.CSS_SELECTOR, ".price_color.align-right")
    PRICE_BOOK = (By.CSS_SELECTOR, ".price_color")
