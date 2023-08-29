from qa_guru_python_07_10.application import app
from qa_guru_python_07_10.data.users import student


def test_simple_registration_form():
    app.open()
    app.left_panel.open_simple_registration_form()

    # When
    app.simple_registration_page.fill_full_user_info(student).submit_form()

    # Then
    app.simple_registration_page.student_should_be_registered(student)
