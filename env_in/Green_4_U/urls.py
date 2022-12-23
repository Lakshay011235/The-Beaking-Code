from django.urls import path
from .views import *
app_name = "Green_4_U"
urlpatterns = [
    path('',Home,name="Home"),
]
