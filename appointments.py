from bs4 import BeautifulSoup
import re
from datetime import datetime

start_date = datetime.strptime('09.03.2023', '%d.%m.%Y')
end_date = datetime.strptime('14.03.2023', '%d.%m.%Y')


class AppointmentParser:
    def __init__(self, html):
        self.html = html
        self.appointments = []

    @staticmethod
    def format_text(text):
        date = text.split()[-1]
        year, month, day = date.split(".")
        time_str = re.search(r'\d{1,2}:\d{2}', text).group(0)
        hour, minute = time_str.split(":")
        hour = hour.zfill(2)
        appointment_datetime = datetime(int(year), int(month), int(day), int(hour), int(minute))
        return appointment_datetime

    def parse(self):
        soup = BeautifulSoup(self.html, "html.parser")
        for div in soup.find_all("div", class_="fc-event fc-event-vert fc-event-start fc-event-end slot-wolny"):
            full = div.find("div", class_="fc-event-inner").text
            self.format_text(full)
            appointment_date = self.format_text(full)
            if start_date <= appointment_date <= end_date:
                self.appointments.append(appointment_date)
            else:
                pass
        return self.appointments
