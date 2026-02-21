import pandas as pd 
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Transaction, AccountEntry, Account
from ..tables import TransactionsTable

def home(request):
    accounts = Account.objects.all()
    transactions = AccountEntry.objects.all()
    
    txn_df = pd.DataFrame(transactions.values())

    graph = TransactionsTable(transactions.values())

    context = {
        "graph": graph
    }

    return render(request, "home.html", context=context)