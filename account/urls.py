from django.urls import path
from . import views
from django.contrib.auth import views as vv



urlpatterns = [
    path('login/',vv.LoginView.as_view(),name="login"),
    
    path('logout/',views.logoutUser,name="logout"),


]
