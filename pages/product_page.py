from .locators import PageObjectLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
#создайте класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках:
class PageObject(BasePage):
    #Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса. Ппроинициализируем новый объект Page и вернем его.При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
    def test_guest_can_add_product_to_basket(self):
        button = self.browser.find_element(*PageObjectLocators.ADD_BUTTON)
        button.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    #Реализуем метод, который будет проверять наличие названия книги
    def should_be_book_name(self):
        ELEMENT_KORZ = self.browser.find_element(*PageObjectLocators.ELEMENT_TEXT_KORZ)
        ELEMENT_BOOK = self.browser.find_element(*PageObjectLocators.ELEMENT_TEXT_BOOK)
        assert ELEMENT_KORZ.text == ELEMENT_BOOK.text, "Book name is not presented"

    def should_be_price(self):
        ELEMENT_KORZ = self.browser.find_element(*PageObjectLocators.PRICE_KORZ)
        ELEMENT_BOOK = self.browser.find_element(*PageObjectLocators.PRICE_BOOK)
        assert ELEMENT_KORZ.text == ELEMENT_BOOK.text, "match the price of the book"

