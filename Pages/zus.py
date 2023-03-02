from selenium.webdriver import Keys
import appointments
from Pages.base_page import BasePage
from Resources.locators import Menu, Appointment
import time


class BookingPage:

    def __init__(self, driver):
        self.driver = driver
        self.zus = BasePage(self.driver)

    def make_reservation(self):
        self.wait_and_click(Menu.SCROLL_DOWN)
        self.wait_and_click(Menu.BOOKING_MAIN)
        self.click_element(Menu.SCROLL_DOWN)
        self.click_element(Menu.BOOKING)
        time.sleep(5)
        self.send_to_element(Appointment.LOCATION, key=Keys.ARROW_DOWN)
        time.sleep(5)
        self.send_to_element(Appointment.LOCATION, key=Keys.ENTER)
        self.click_element(Appointment.TYPE_OF_VISIT_MAIN)
        self.click_element(Appointment.TYPE_OF_VISIT)
        self.click_element(Appointment.NEXT_BUTTON)
        self.wait_element(Appointment.AGENDA)
        self.click_element(Appointment.NEXT_DATE_BUTTON)
        self.wait_element(Appointment.AGENDA)
        self.click_element(Appointment.NEXT_DATE_BUTTON)
        self.wait_element(Appointment.AGENDA)
        self.click_element(Appointment.NEXT_DATE_BUTTON)
        time.sleep(5)
        html = self.get_html()

        parser = appointments.AppointmentParser(html)
        parser.parse()
        dates = [d.strftime("%Y-%m-%d %H:%M") for d in parser.appointments]
        print(dates)
