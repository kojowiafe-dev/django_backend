from django.test import TestCase
from django.contrib.auth import get_user_model
from api.models import Event, Attendee, Sermon, PrayerRequest
from datetime import date


User = get_user_model()

class UserModelTest(TestCase):
    def test_user_model_exists(self):
        users = User.objects.count()

        self.assertEqual(users, 0)

    def test_model_has_string_representation(self):
        user = User.objects.create(role='admin')

        self.assertEqual(str(user), user.role)



class EventModelTest(TestCase):
    def test_event_model_exists(self):
        events = Event.objects.count()

        self.assertEqual(events, 0)


    def test_event_has_all_fields(self):
        user = User.objects.create_user(username='creator_user', password='200509')
        event = Event.objects.create(title='Serve GOD', creator=user)

        self.assertEqual(str(event), event.title)
        self.assertEqual(user, event.creator)



class AttendeeModelTest(TestCase):
    def test_attendee_model_exists(self):
        attendee = Attendee.objects.count()

        self.assertEqual(attendee, 0)


    def test_attendee_model_has_all_fields(self):
        user = User.objects.create_user(username='user', password='200509')
        event = Event.objects.create(title='Serve GOD', creator=user)
        attendee = Attendee.objects.create(status='Present', user=user, event=event)

        self.assertEqual(str(attendee), attendee.status)
        self.assertEqual(user, attendee.user)
        self.assertEqual(user, event.creator)
        self.assertEqual(event, attendee.event)



class SermonModelTest(TestCase):
    def test_sermon_model_exists(self):
        sermons = Sermon.objects.count()

        self.assertEqual(sermons, 0)


    def test_sermon_model_has_all_fields(self):
        user = User.objects.create_user(username='user', password='200509')
        sermon = Sermon.objects.create(title='Love GOD', creator=user)

        self.assertEqual(str(sermon), sermon.title)
        self.assertEqual(user, sermon.creator)



class ChurchRoleTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', email='admin@gmail.com', date_of_birth='2025-08-04', password='200509', role='admin')
        self.member = User.objects.create_user(username='member', password='200509', role='member')
        self.pastor = User.objects.create_user(username='pastor', password='200509', role='pastor')
        self.sermon = Sermon.objects.create(title='Faith', creator=self.pastor)


    def test_sermon_create_by_pastor(self):
        self.assertEqual(str(self.sermon), self.sermon.title)
        self.assertEqual(self.pastor, self.sermon.creator)
        self.assertEqual(self.pastor.role, 'pastor')

        # print(type(self.pastor))


    def test_pastor_is_a_valid_user(self):
        self.assertIsInstance(self.sermon.creator, User)
        # print(f"User type is {type(User)}")
        # print(f"Pastor type is {type(self.pastor)}")



    def test_prayer_request_by_members(self):
        prayer_request = PrayerRequest.objects.create(title='Prayer for protection', member=self.member)

        self.assertEqual(prayer_request.title, 'Prayer for protection')
        self.assertTrue('protection' in prayer_request.title)


    
    def test_member_cannot_create_sermon_directly(self):
        if self.member.role != 'pastor':
            with self.assertRaises(Exception):
                Sermon.objects.create(
                    title='Love your neighbour',
                    preacher=self.member
                )

    # print(type(str(date.today())))
    def test_user_birthday(self):
        self.assertEqual(self.admin.date_of_birth, str(date.today()))