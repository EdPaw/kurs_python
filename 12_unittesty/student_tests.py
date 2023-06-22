import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('-----------setUpClass----------')

    def setUp(self) -> None:
        print('-----------setUp----------')

    def test_email_change(self):
        # GIVEN
        anna = Student('anna', 'snow', 4.6, True)
        expected_email = 'anna.snow@uam.com'
        self.assertEqual(anna.email, expected_email)

        # WHEN
        anna.last = 'summer'

        # THEN
        new_expected_email = 'anna.summer@uam.com'
        self.assertEqual(anna.email, new_expected_email)

    def test_full_name_change(self):
        anna = Student('anna', 'snow', 4.6, True)
        expected_fullname = 'Anna Snow'
        self.assertEqual(anna.fullname, expected_fullname)

        anna.name = 'emily'
        anna.last = 'summer'

        new_expected_fullname = 'Emily Summer'
        self.assertEqual(anna.fullname, new_expected_fullname)

    def test_grant_scholarship(self):
        anna = Student('anna', 'snow', 4.6, True)
        anna.grant_scholarship()
        self.assertEqual(anna.scholarship, True)

        anna.student_avg = 3.6
        anna.grant_scholarship()
        self.assertEqual(anna.scholarship, False)

    def tearDown(self) -> None:
        print('-----------tearDown----------')

    @classmethod
    def tearDownClass(cls) -> None:
        print('-----------terDownClass----------')
