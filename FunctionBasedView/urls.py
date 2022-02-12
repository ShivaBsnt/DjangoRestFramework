from django.urls import path
from .views import get_post_student

urlpatterns = [
    path('student/', get_post_student, name='student'),
]
