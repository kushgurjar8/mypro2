from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('about/', views.about, name='about'),
    path('student-list/', views.student_list, name='student_list'),
    
]