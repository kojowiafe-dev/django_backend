from django.contrib.auth import get_user_model
from .models import Event, Attendee, Sermon, PrayerRequest, Announcements
from rest_framework import serializers
from ..accounts import models


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'date_of_birth']

    def create(self, validated_data):
        return models.CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user'),
            date_of_birth=validated_data.get('date_of_birth')
        )

    
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'

    
class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = '__all__'


# class BirthDaySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = BirthDay
#         fields = '__all__'


class AnnouncementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'