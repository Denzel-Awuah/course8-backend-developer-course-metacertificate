from django.test import TestCase
from django.urls import reverse
from .models import Booking, Menu
from .forms import BookingForm

# Create your tests here.
class BookingViewTest(TestCase):
    def setUp(self):
        # Create some Bookings for testing
        Booking.objects.create(first_name="name1", reservation_date="2024-05-10", reservation_slot=1)
        Booking.objects.create(first_name="name2", reservation_date="2024-06-10", reservation_slot=2)

    def test_view_url_exists_at_about_page(self):
        # Test that the view is accessible at the expected url
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Test that the view uses the correct template
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')


class BookingModelTest(TestCase):
    def setUp(self):
        # Create a Booking for testing
        self.Booking = Booking.objects.create(first_name="name1", reservation_date="2024-05-10", reservation_slot=1)

    def test_Booking_creation(self):
        # Test that the Booking is created with the correct attributes
        self.assertTrue(isinstance(self.Booking, Booking))
        self.assertEqual(self.Booking.first_name, "name1")
        self.assertEqual(self.Booking.reservation_date, "2024-05-10")

    def test_Booking_str(self):
        # Test that the Booking has a string representation
        self.assertEqual(str(self.Booking), "name1")

class MenuItemTest(TestCase):
    def setUp(self):
        # Create a Booking for testing
        self.Menu = Menu.objects.create(name="item1", price=1, menu_item_description="the menu item description")

    def test_MenuItem_creation(self):
        # Test that the MenuItem is created with the correct attributes
        self.assertTrue(isinstance(self.Menu, Menu))
        self.assertEqual(self.Menu.name, "item1")
        self.assertEqual(self.Menu.price, 1)

    def test_MenuItem_str(self):
        # Test that the Booking has a string representation
        self.assertEqual(str(self.Menu), "item1")
