
from serializer import UserSerializer, CategorySerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from models import User, Category, Task
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users = self.get_object()
        return Response(users)

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return Response(category)

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        tasks = self.get_object()
        return Response(tasks)

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

