from rest_framework.generics import ListAPIView,\
    CreateAPIView
from Common.models import Student
from Common.serializers import StudentSerializer


class StudentGenericListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGenericCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
