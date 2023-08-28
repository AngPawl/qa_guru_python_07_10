import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_month: str
    birth_year: str
    birth_day: str
    subjects: str
    hobbies: str
    picture_path: str
    address: str
    state: str
    city: str


student = User(
    first_name='John',
    last_name='Doe',
    email='test_email.demoqa@test.com',
    gender='Male',
    phone_number='8800111111',
    birth_month='January',
    birth_year='2000',
    birth_day='01',
    subjects='Computer Science',
    hobbies='Sports',
    picture_path='student.png',
    address='42 Best street, suite 1, Dallas, TX, 11111',
    state='NCR',
    city='Delhi',
)
