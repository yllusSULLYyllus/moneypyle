from django.urls import path
from . import views

app_name = "moneypyle"

urlpatterns = [
    path("journal/", views.new_entry, name="journal"),
    path("accounts/", views.add_account, name="accounts"),
    path("accounts/<int:account_id>", views.account_details, name="account_details"),
    path("", views.home, name="home"),
    path("signon/", views.signon, name='signon')
]