from .base_page import BasePage
from selenium.webdriver.common.by import By
#создайте класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
class MainPage(BasePage):
    #Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    #Реализуем метод, который будет проверять наличие ссылки
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
