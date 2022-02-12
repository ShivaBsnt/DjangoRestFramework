from rest_framework.response import Response
from rest_framework.views import APIView
from Common.serializers import StudentSerializer
from Common.models import Student


class StudentAPIView(APIView):
    """List all students, or create a new student."""
    def get(self, request, format=None):
        # gets all student objects from database
        student = Student.objects.all()
        # sends queryset for serialization
        serializer = StudentSerializer(student, many=True)
        # sends data obtained from serializer into response
        return Response(serializer.data)

    def post(self, request, format=None):
        # sends data requested for deserialization
        serializer = StudentSerializer(data=request.data)
        # validates requested data
        serializer.is_valid(raise_exception=True)
        # saves data to database
        serializer.save()
        # returns saved data as a response
        return Response(serializer.data)
