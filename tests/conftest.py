import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """
        Опция командной строки.
        В командную строку передается параметр вида '--browser_name="firefox"'
        По умолчанию передается параметр, запускающий Chrome браузер
    """
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()

    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser..")
    browser.quit()
