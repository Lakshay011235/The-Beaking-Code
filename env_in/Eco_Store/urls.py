from django.urls import path
from .views import *

app_name = "Eco_Store"
urlpatterns = [
    path('',Home,name="Home"),
    path('prod/',Product,name="Product"),
]
