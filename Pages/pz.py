from selenium.webdriver import Keys
from Pages.base_page import BasePage
from Resources.data import Data
from Resources.locators import Pz


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.pz_main = BasePage(self.driver)

    def login(self):
        self.click_element(Pz.BUTTON)
        self.send_to_element(Pz.LOGIN, Data.login)
        self.send_to_element(Pz.PASSWORD, Data.password, Keys.ENTER)
