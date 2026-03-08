from .models import Students
from .serializers import Studentserializers
from rest_framework import generics,mixins

class AllStudentAPI(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset=Students.objects.all()
    serializer_class=Studentserializers
    #Reading Data
    def get(self,request,*arg,**kwargs):
        return self.list(request,*arg,**kwargs)
    #creating New data
    def post(self,request,*arg,**kwargs):
        return self.create(request,*arg,**kwargs)
    
class SingleStudentApi(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset=Students.objects.all()
    serializer_class=Studentserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
