from django.urls import path
from . import views
urlpatterns = [
    path('',views.Welcome_View,name="Welcome_View"),
    path('courses/', views.Courses_Info, name="Courses_Info"),
]
