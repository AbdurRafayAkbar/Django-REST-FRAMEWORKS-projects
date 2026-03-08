from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializers

class StudentApi(APIView):
    def get(self,request,pk=None):
        if pk:
            try:
                student=Students.objects.get(id=pk)
                serializer=StudentsSerializers(student)
                return Response(serializer.data)
            except Students.DoesNotExist:
                return Response({"message": "No Student Exists!"})
        else:
            student=Students.objects.all()
            serializer=StudentsSerializers(student,many=True)
            return Response(serializer.data)
    def post(self,request):
        serializer=StudentsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New student added Succesfully"})
    def put(self,request,pk):
        try:
            student=Students.objects.get(id=pk)
        except Students.DoesNotExist:
            return Response({"message": "No Student Exists!"})
        serializer=StudentsSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{"message":"student updated Succesfully"})
        else:
            return Response(serializer.errors,{"message":"Error"})

    def delete(self,pk,request):
        try:
            student=Students.objects.get(id=pk)
            student.delete()
            return Response({"message":"Delted Succesfully!"})
        except:
            return Response({"message":"STudent Doesn't Exists."})
