from django.urls import path
from . import views

app_name = "moneypyle"

urlpatterns = [
    path('list/', views.AccountView.as_view(), name='list'),
    path("journal/", views.journal.as_view(), name="journal")
]