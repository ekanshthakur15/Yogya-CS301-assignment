from django.test import TestCase
from django.contrib.auth.models import User
from .models import Exhibit, Event, Talent

# Create your tests here.

class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.exhibit = Exhibit.objects.create(
            title='Test Exhibit',
            description='A test exhibit',
            location='Test Location'
        )

        self.exhibit.save()

        self.event = Event.objects.create(
            title='Test Event',
            description='A test event',
            date='2023-04-01',
        )

        self.event.save()

        self.talent = Talent.objects.create(
            name='Test Talent',
            contact_info='test@example.com',
        )

        self.talent.save()


    def test_exhibit_str(self):
        self.assertEqual(str(self.exhibit), 'Test Exhibit')

    def test_event_str(self):
        self.assertEqual(str(self.event), 'Test Event')

    def test_talent_str(self):
        self.assertEqual(str(self.talent), 'Test Talent')

    def test_review_exhibit(self):
        review = Exhibit.objects.create(
            title='Test Exhibit review by testuser',
            description ='A test review'
        )

        self.assertEqual(str(review), 'Test Exhibit review by testuser')

    def test_review_event(self):
        review = Event.objects.create(
            title='Test Event review by testuser',
            description ='A test review',
        )

        self.assertEqual(str(review), 'Test Event review by testuser')

    def test_review_talent(self):
        review = Talent.objects.create(
            name='Test Talent review by testuser',
            contact_info='A test review'
        )

        self.assertEqual(str(review), 'Test Talent review by testuser')

    def test_favorite_exhibit(self):
        favorite = Exhibit.objects.create(
            user=self.user,
            exhibit=self.exhibit
        )

        self.assertEqual(str(favorite), 'Test Exhibit favorite by testuser')
