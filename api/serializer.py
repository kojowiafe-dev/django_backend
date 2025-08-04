from django.contrib.auth import get_user_model
from .models import Event, Attendee, Sermon, PrayerRequest, Announcements
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role', 'date_of_birth']
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
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