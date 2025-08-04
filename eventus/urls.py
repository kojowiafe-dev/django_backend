from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, CreateEventView, CreateAttendeeView, CreateSermonView, CreateAnnouncementsView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/login/', LoginView.as_view(), name='login'),
    # path('api/users/login/', obtain_auth_token, name='login'),
    path('api/users/register/', CreateUserView.as_view(), name='register'),
    path('api/events/create/', CreateEventView.as_view(), name='create_event'),
    path('api/attendees/register/', CreateAttendeeView.as_view(), name='register_attendee'),
    path('api/sermons/create/', CreateSermonView.as_view(), name='create_sermon'),
    path('api/announcements/create/', CreateAnnouncementsView.as_view(), name='create_announcements'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]
