from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('addCourse/',views.addCourse,name="addCourse"),
    path('addCourse/processAddCourse',views.processAddCourse,name="processAddCourse"),
    path('course/<str:courseId>/', views.course, name='course'),
    path('courses', views.allCourses, name='allCourse'),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout")

]
