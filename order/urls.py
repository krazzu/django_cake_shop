from django.urls import path
from .views import order

app_name = 'order'

urlpatterns = [
    path('', order, name='order'),
]