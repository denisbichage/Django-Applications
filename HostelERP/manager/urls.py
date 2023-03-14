from django.conf.urls import url, include
from . import views
from django.views.generic import ListView
from .models import EmployeeInfo

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=EmployeeInfo.objects.all(), template_name="displayaccounts.html")),
    url(r'^register/$', views.register, name='register'),
    url(r'^startsession/$', views.startsession, name='startsession'),
    url(r'^update/$', views.update, name='update'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]