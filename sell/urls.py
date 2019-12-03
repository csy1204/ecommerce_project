from django.urls import path
from .views import *

urlpatterns = [
   path('', PhotoListView.as_view(), name='register')
]