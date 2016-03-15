
from serializer import UserSerializer, CategorySerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from models import User, Category, Task
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryList(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskList(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })