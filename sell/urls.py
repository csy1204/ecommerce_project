from django.urls import path
from .views import *

app_name = 'sell'

urlpatterns = [
   path('', PhotoListView.as_view(), name='register')
]