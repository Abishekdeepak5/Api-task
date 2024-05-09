from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
# Create your views here.
def index(request):
    return render(request,'index.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

