import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.base_page import BasePage
from Resources.locators import Pz, Menu, Appointment
from Resources.data import Data
import appointments


class AppointmentScheduler(BasePage):
    def __init__(self):
        self.webdriver_service = Service('C:\chromedriver\chromedriver.exe')
        self.options = Options()
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.options)
        self.driver.implicitly_wait(15)

    def schedule_availability(self):
        self.open(Data.url)
        pz_main = BasePage(self.driver)
        pz_main.click_element(Pz.BUTTON)
        pz_main.send_keys_to_element3(Pz.LOGIN, Data.login)
        pz_main.send_keys_to_element3(Pz.PASSWORD, Data.password, Keys.ENTER)

        zus = BasePage(self.driver)
        zus.wait_and_click(Menu.SCROLL_DOWN)
        zus.wait_and_click(Menu.BOOKING_MAIN)
        zus.click_element(Menu.SCROLL_DOWN)
        zus.click_element(Menu.BOOKING)
        time.sleep(5)
        zus.send_keys_to_element3(Appointment.LOCATION, key=Keys.ARROW_DOWN)
        time.sleep(5)
        zus.send_keys_to_element3(Appointment.LOCATION, key=Keys.ENTER)
        zus.click_element(Appointment.TYPE_OF_VISIT_MAIN)
        zus.click_element(Appointment.TYPE_OF_VISIT)
        zus.click_element(Appointment.NEXT_BUTTON)
        zus.wait_element(Appointment.AGENDA)
        zus.click_element(Appointment.NEXT_DATE_BUTTON)
        zus.wait_element(Appointment.AGENDA)
        zus.click_element(Appointment.NEXT_DATE_BUTTON)
        zus.wait_element(Appointment.AGENDA)
        zus.click_element(Appointment.NEXT_DATE_BUTTON)
        time.sleep(5)
        html = zus.get_html()
        self.driver.quit()

        parser = appointments.AppointmentParser(html)
        parser.parse()
        dates = [d.strftime("%Y-%m-%d %H:%M") for d in parser.appointments]
        print(dates)


if __name__ == '__main__':
    obj = AppointmentScheduler()
    obj.schedule_availability()
