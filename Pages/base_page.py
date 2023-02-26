from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()

    def wait_and_click(self, locator):
        self.wait_element(locator)
        self.click_element(locator)

    def send_to_element(self, locator, text=None, key=None):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        if text is not None and key is not None:
            element.send_keys(text, key)
        elif text is not None:
            element.send_keys(text)
        elif key is not None:
            element.send_keys(key)

    def wait_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print("Fail")
            self.driver.quit()

    def get_html(self):
        return self.driver.page_source
