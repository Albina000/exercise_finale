import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# с помощью pytest_addoption и фикстуры request настраиваем тестовое окружение (передача параметров через командную строку)
# добавим обработчик опций
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose a language.")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language") # для запроса значения параметра
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


