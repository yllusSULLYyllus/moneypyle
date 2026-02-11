from django.shortcuts import render
from django.views.generic import ListView
from .models import Account

class AccountView(ListView):
    model = Account
    template_name = 'accounts/list.html'
    

