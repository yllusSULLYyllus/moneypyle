from django.urls import path
from . import views

app_name = "moneypyle"

urlpatterns = [
    path('', views.AccountView.as_view(), name='list')
]