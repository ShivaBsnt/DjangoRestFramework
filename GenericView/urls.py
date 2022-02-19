from django.urls import path
from .views import StudentGenericListAPIView, StudentGenericCreateAPIView

urlpatterns = [
    path('student/list/', StudentGenericListAPIView.as_view(), name='student'),
    path('student/create/', StudentGenericCreateAPIView.as_view(), name='student'),
]

