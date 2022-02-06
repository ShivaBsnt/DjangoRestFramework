from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Common.serializers import StudentSerializer
from Common.models import Student


@api_view(['GET', 'POST'])
def get_post_student(request):
    if request.method.lower() == 'get':
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data)

    if request.method.lower() == 'post':
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def retrieve_patch_delete_student(request, pk):

    if request.method.lower() == 'get':
        instance = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance)
        return Response(serializer.data)

    if request.method.lower() == 'patch':
        instance = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method.lower() == 'delete':
        instance = Student.objects.get(id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
