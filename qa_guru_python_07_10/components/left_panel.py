from selene import browser, have

from qa_guru_python_07_10.pages.simple_registration_page import SimpleRegistrationPage


class LeftPanel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, header, item):
        self.container.all('.group-header').element_by(have.text(header)).click()
        self.container.all('.menu-list .text').element_by(have.text(item)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
        return SimpleRegistrationPage()
