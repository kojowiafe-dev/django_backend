from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
import uuid



class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Attendee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status
    
    
class Sermon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    media_url = models.URLField(max_length=100)
    preacher = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class PrayerRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Announcements(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateField