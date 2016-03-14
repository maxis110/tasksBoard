
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from serializer import UserSerializer, CategorySerializer, TaskSerializer
from models import User, Category, Task


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer

class TaskList(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })

