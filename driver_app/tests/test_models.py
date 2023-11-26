from django.test import TestCase
from driver_app.models import Driver

class DriverModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Driver.objects.create(name='Penelope Clearwater', address='Hogwarts', email='pclearwater@hogwarts.edu')

    def test_name_label(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def test_address_label(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'Address')

    def test_email_label(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Email Address')

    def test_name_max_length(self):
        driver = Driver.objects.get(id=1)
        max_length = driver._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_address_max_length(self):
        driver = Driver.objects.get(id=1)
        max_length = driver._meta.get_field('address').max_length
        self.assertEqual(max_length, 200)

    def test_email_max_length(self):
        driver = Driver.objects.get(id=1)
        max_length = driver._meta.get_field('email').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        driver = Driver.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(driver.get_absolute_url(), '/driver/1/')