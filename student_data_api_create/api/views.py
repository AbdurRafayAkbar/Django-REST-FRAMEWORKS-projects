from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

@api_view(["POST"])
def student_list(request):
    
    student=StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
        return Response(student.data)
    return Response(student.errors)


