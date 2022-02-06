from django.urls import path
from .views import get_post_student, retrieve_patch_delete_student

urlpatterns = [
    path('student/', get_post_student, name='student'),
    path('student/<int:pk>/', retrieve_patch_delete_student, name='student')
]
