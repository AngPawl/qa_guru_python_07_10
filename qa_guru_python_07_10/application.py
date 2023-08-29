from selene import browser

from qa_guru_python_07_10.components.left_panel import LeftPanel
from qa_guru_python_07_10.pages.registration_page import RegistrationPage
from qa_guru_python_07_10.pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.simple_registration_page = SimpleRegistrationPage()
        self.left_panel = LeftPanel()

    def open(self):
        browser.open('/forms')


app = ApplicationManager()
