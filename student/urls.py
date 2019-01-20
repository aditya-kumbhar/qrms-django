from django.urls import path,include
from . import views

urlpatterns = [
    path('courses/',views.courses,name="courses"),
    path('home/',views.home, name="home"),
    path('',views.index,name = "index"),

    # path('stud_login/',views.stud_login,name = "stud_login"),
    # path('stud_logout/',views.logout, name="stud_logout"),
    
]