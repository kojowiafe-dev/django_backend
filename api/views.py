from .models import Event, Attendee, Sermon, Announcements
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .serializer import UserSerializer, EventSerializer, AttendeeSerializer, SermonSerializer, AnnouncementsSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import obtain_auth_token



User = get_user_model()
class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializedData = UserSerializer(users, many=True).data
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializedData = UserSerializer(user).data
    except not User.objects.get(pk=pk).exists():
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except not User.objects.get(pk=pk).exists():
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializedData = EventSerializer(events, many=True).data
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        serializedData = EventSerializer(event).data
    except not User.objects.get(pk=pk).exists():
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Event found"}, serializedData, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        # serializedData = EventSerializer(event).data
    except not Event.objects.get(pk=pk).exists():
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Event found successfully"}, status=status.HTTP_200_OK)



class CreateAttendeeView(generics.CreateAPIView):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
def get_attendees(request):
    attendees = Attendee.objects.all()
    serializedData = AttendeeSerializer(attendees, many=True).data
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_attendee(request, pk):
    try:
        attendee = Attendee.objects.get(pk=pk)
        serializedData = AttendeeSerializer(attendee).data
    except not Attendee.objects.get(pk=pk).exists():
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Attendee found successfully"}, serializedData, status=status.HTTP_200_OK)



@api_view(['DELETE'])
def delete_attendee(request, pk):
    try:
        attendee = Attendee.objects.get(pk=pk)
        serializedData = AttendeeSerializer(attendee).data
    except not Attendee.objects.get(pk=pk).exists():
        return Response({"error": "Attendee not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Attendee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class EventAttendeeListView(generics.ListAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Attendee.objects.filter(event__id=event_id)
    

class CreateSermonView(generics.CreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAuthenticated]



@api_view(['GET'])
def get_sermons(request):
    sermons = Sermon.objects.all()
    serializedData = SermonSerializer(sermons, many=True).data
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sermon(request, pk):
    try:
        sermons = Sermon.objects.get(pk=pk)
        serializedData = SermonSerializer(sermons).data
    except not Sermon.objects.get(pk=pk).exists():
        return Response({"error": "Sermon not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializedData, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_sermon(request, pk):
    try:
        sermon = Sermon.objects.get(pk=pk)
        serializedData = SermonSerializer(sermon).data
    except not Sermon.objects.get(pk=pk).exists():
        return Response({"error": "Sermon not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": "Sermon deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


from datetime import date
@api_view(['GET'])
def get_birthdays(request):
    users = User.objects.all()
    serializedData = UserSerializer(users, many=True).data

    today_date = [i for i in str(date.today())][-2:]
    today_month = [i for i in str(date.today())][5:7]
    # date_of_birth = [[i for i in info["date_of_birth"]] for info in serializedData if info["date_of_birth"][-2:] == today_date]

    results = [info for info in serializedData if [i for i in info["date_of_birth"]][-2:] == today_date and [i for i in info["date_of_birth"]][5:7] == today_month]

    return Response(results, status=status.HTTP_200_OK)


class CreateAnnouncementsView(generics.CreateAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializers
    permission_classes = [IsAuthenticated]


# class GetBirthdayList(generics.ListAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         date_of_birth = self.kwargs['date_of_birth']
#         return User.objects.filter(date_of_birth==str(date.today()))
    

# class EventAttendeeListView(generics.ListAPIView):
#     serializer_class = AttendeeSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         event_id = self.kwargs['event_id']
#         return Attendee.objects.filter(event__id=event_id)


# @api_view(['GET'])
# def get_event_attendees(request, event_id):
#     try:
#         event = Event.objects.get(pk=event_id)
#         attendees = event.attendees.all()
#         serializedData = AttendeeSerializer(attendees, many=True).data
#     except not Event.objects.get(pk=event_id).exists():
#         return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
#     return Response(serializedData, status=status.HTTP_200_OK)