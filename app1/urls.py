from django.urls import path,include
from app1.views import *
app_name='any'

urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'), 
    ]