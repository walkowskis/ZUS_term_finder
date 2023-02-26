from selenium.webdriver.common.by import By


class Pz:
    BUTTON = (By.XPATH, "//strong[text()='Profil Zaufany']")
    LOGIN = (By.ID, "loginForm:login")
    PASSWORD = (By.ID, "loginForm:hasło")
    FORM_BUTTON = (By.ID, "loginForm:loginButton")


class Menu:
    SCROLL_DOWN = (By.CSS_SELECTOR, 'div#scrollDownButton>div')
    BOOKING_MAIN = (By.XPATH, '//span[text()="Rezerwacja wizyty w ZUS"]')
    BOOKING = (By.XPATH, '//td[text()="Rezerwacja wizyty"]')
    LAST_ELEMENT = (By.XPATH, "//div[@class='zusnpiMenuPaneIconNode hotelMenuIcon']")


class Appointment:
    LOCATION = (By.XPATH, '//input[@title="Adres jednostki"]')
    TYPE_OF_VISIT_MAIN = (By.XPATH, '// option[ @ value = "1700"]')
    TYPE_OF_VISIT = (By.XPATH, '//select[@dojoattachevent="onchange:onChangePodgrupy"]//option[1]')
    NEXT_BUTTON = (By.CLASS_NAME, 'zusnpiReturnLink_nextA')
    NEXT_DATE_BUTTON = (By.CLASS_NAME, 'next')
    AGENDA = (By.XPATH, "//td[contains(@class,'fc-agenda-gutter fc-widget-content')]")
