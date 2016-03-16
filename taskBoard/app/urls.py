from django.conf.urls import url
from serializer import UserSerializer, TaskSerializer, CategorySerializer
from models import User, Task, Category
from rest_framework.generics import ListCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^users/$', ListCreateAPIView.as_view(queryset= User.objects.all(), serializer_class = UserSerializer), name='user-list'),
    url(r'^tasks/$', ListCreateAPIView.as_view(queryset= Task.objects.all(), serializer_class = TaskSerializer), name='task-list'),
    url(r'^category/$', ListCreateAPIView.as_view(queryset= Category.objects.all(), serializer_class = CategorySerializer), name='category-list'),
])