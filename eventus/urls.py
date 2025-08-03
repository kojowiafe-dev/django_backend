from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, CreateEventView, CreateAttendeeView, CreateSermonView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/user/register/', CreateUserView.as_view(), name='register'),
    path('api/users/register/', CreateUserView.as_view(), name='register'),
    path('api/events/create/', CreateEventView.as_view(), name='create_event'),
    path('api/attendees/register/', CreateAttendeeView.as_view(), name='register_attendee'),
    path('api/sermons/create/', CreateSermonView.as_view(), name='create_sermon'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]
