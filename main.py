from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.base_page import BasePage
from Resources.data import Data
from Pages.pz import LoginPage
from Pages.zus import BookingPage


class AppointmentScheduler(BasePage):

    def __init__(self, headless=True):
        self.webdriver_service = Service(Data.driver_path)
        self.options = Options()
        self.options.add_argument('--window-size=1920,1080')
        if headless:
            self.options.add_argument('headless')
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.options)
        self.driver.implicitly_wait(15)

    def schedule_availability(self):
        self.open(Data.url)

        login_page = LoginPage(self.driver)
        login_page.login()

        booking_page = BookingPage(self.driver)
        booking_page.make_reservation()


if __name__ == '__main__':
    obj = AppointmentScheduler()
    obj.schedule_availability()
