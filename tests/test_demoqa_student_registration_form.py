from qa_guru_python_07_10.pages.registration_page import RegistrationPage


def test_successful_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # When
    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Doe')
    registration_page.fill_user_email('test_email.demoqa@test.com')
    registration_page.fill_gender('Male')
    registration_page.fill_phone_number('8800111111')
    registration_page.fill_date_of_birth('January', '2000', 1)
    registration_page.fill_subjects('computer')
    registration_page.fill_hobbies('Sports')
    registration_page.upload_picture('student.png')
    registration_page.fill_current_address('42 Best street, suite 1, Dallas, TX, 11111')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit_form()

    # Then
    registration_page.modal_form_pops_up()
    registration_page.student_should_be_registered(
        'John Doe',
        'test_email.demoqa@test.com',
        'Male',
        '8800111111',
        '01 January,2000',
        'Computer Science',
        'Sports',
        'student.png',
        '42 Best street, suite 1, Dallas, TX, 11111',
        'NCR Delhi',
    )
