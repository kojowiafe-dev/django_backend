from django.urls import path, include
from .views import CreateUserView, get_users, delete_user, get_user, CreateEventView, get_events, get_event, delete_event, CreateAttendeeView, get_attendee, get_attendees, delete_attendee, EventAttendeeListView, get_sermon, get_sermons, delete_sermon, get_birthdays

urlpatterns = [
    # path('users/create/', CreateUserView.as_view(), 'add_user'),
    path('users/', get_users, name='get_users'),
    path('users/delete/<int:pk>/', delete_user, name='delete_user'),
    path('users/<int:pk>/', get_user, name='get_user'),
    path('users/birthdays/', get_birthdays, name='get_birthdays'),
    # path('events/create/', CreateEventView.as_view(), 'add_event'),
    path('events/', get_events, name='get_events'),
    path('events/delete/<int:pk>/', delete_event, name='delete_event'),
    path('events/<int:pk>/', get_event, name='get_event'),
    path('attendees/', get_attendees, name='get_attendees'),
    path('attendees/<int:pk>/', get_attendee, name='get_attendee'),
    path('attendees/delete/<int:pk>/', delete_attendee, name='delete_attendee'),
    path('events/<uuid:event_id>/attendees/', EventAttendeeListView.as_view(), name='event_attendee'),
    path('sermons/', get_sermons, name='get_sermons'),
    path('sermons/<uuid:pk>/', get_sermon, name='get_sermon'),
    path('sermons/delete/<int:pk>/', delete_sermon, name='delete_sermon'),
]
