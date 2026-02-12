from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Account, AccountEntry

class AccountView(ListView):
    model = Account
    template_name = 'accounts/list.html'

class journal(CreateView):
    model = AccountEntry
    fields = ['account_id', 'credit_amount']
    template_name = "transactions/journal.html"
