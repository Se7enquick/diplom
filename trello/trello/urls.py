
from django.contrib import admin
from django.urls import path, include

from authentication.views import registration
from django.contrib.auth import views as auth_views

app_name = 'trello'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration, name = 'register'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('', include('main.urls'))
]

