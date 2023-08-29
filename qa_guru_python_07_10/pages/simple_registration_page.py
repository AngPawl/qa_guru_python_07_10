from selene import browser, command, have


class SimpleRegistrationPage:
    def __init__(self):
        self.registration_result = browser.element('#output')

    def open(self):
        browser.open('/text-box')

        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.8)"'
        )

        return self

    def fill_full_user_info(self, user):
        self._fill_name(f'{user.first_name} {user.last_name}')
        self._fill_email(user.email)
        self._fill_current_address(user.address)
        self._fill_permanent_address(user.address)

        return self

    def _fill_name(self, name):
        browser.element('#userName').type(name)

    def _fill_email(self, email):
        browser.element('#userEmail').type(email)

    def _fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def _fill_permanent_address(self, address):
        browser.element('#permanentAddress').type(
            '42 Best street, suite 1, Dallas, TX, 11111'
        )

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def student_should_be_registered(self, user):
        self.registration_result.element('#name').should(
            have.text(f'{user.first_name} {user.last_name}')
        )
        self.registration_result.element('#email').should(have.text(user.email))
        self.registration_result.element('#currentAddress').should(
            have.text(user.address)
        )
        self.registration_result.element('#permanentAddress').should(
            have.text(user.address)
        )
