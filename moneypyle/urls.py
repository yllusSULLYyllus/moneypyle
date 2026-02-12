from django.urls import path
from . import views

app_name = "moneypyle"

urlpatterns = [
    path('list/', views.add_account, name='add_account'),
    path("journal/", views.new_entry, name="journal"),
    path("account/", views.add_account, name="account"),
    path("account/<int:account_id>", views.account_details, name="account_details"),
    path("", views.home, name="home")
]