from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import StudentAPIView

urlpatterns = [
    path('student/', StudentAPIView.as_view(), name='student'),
]
format_suffix_patterns(urlpatterns)
