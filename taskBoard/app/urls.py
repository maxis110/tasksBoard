from django.conf.urls import url
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^tasks/$', views.TaskList.as_view(), name='task-list'),
    url(r'^category/$', views.CategoryList.as_view(), name='category-list'),
])