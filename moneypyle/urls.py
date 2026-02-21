from django.urls import path
from . import views

app_name = "moneypyle"

urlpatterns = [
    path("journal/", views.new_entry, name="journal"),
    path("admin/", views.admin_home, name="admin-home"),
    path("accounts/", views.add_account, name="accounts"),
    path("accounts/<int:account_id>", views.account_details, name="account_details"),
    path("", views.home, name="home"),
    path("clock-time/", views.clock_time, name='clock-time'),
    path("party/", views.party_home, name='party'),
    path("signon/", views.signon, name='signon')
]