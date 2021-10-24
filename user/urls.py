
from django.urls import path
from . import views as user_view
from django.contrib.auth import views as auth_views
app_name = "account"

urlpatterns = [
    path('register/',user_view.register,name="register"),
    path('',auth_views.LoginView.as_view(template_name="user/login.html") , name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="user/logout.html"),name="logout"),
    path('profile/',user_view.profile , name="profile"),
    path('profile_update/',user_view.profile_update , name="update")
]