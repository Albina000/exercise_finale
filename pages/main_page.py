from .locators import MainPageLocators
from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
#создайте класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
class MainPage(BasePage):
    #Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
    #Реализуем метод, который будет проверять наличие ссылки
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    #Реализуем метод, который будет проверять наличие login в текущем url браузера
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in current_url from browser"
    #Реализуем метод, который будет проверять наличие формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    #Реализуем метод, который будет проверять наличие формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
