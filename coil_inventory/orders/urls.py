from django.urls import path
from .views import SalesOrderCreate

urlpatterns = [
    path('create/', SalesOrderCreate.as_view()),
]
