from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.http.request import QueryDict
from django.views.generic import ListView, CreateView, DetailView
from django.forms.models import modelformset_factory
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
import pandas as pd

from .models import Account, AccountEntry
from .forms import TransactionForm, AccountForm, EntryForm, EntryFormSet

class AccountView(ListView):
    model = Account
    template_name = 'accounts/list.html'
    fields = ['name']

def home(request):
    return render(request, "home.html")

def signon(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "Invalid Login Information"
            }
            return render(request, 'signon.html', context=context)
        login(request, user)
        return redirect('moneypyle:home')

    return render(request, 'signon.html')

def signoff(request):   
    return render(request, 'signon.html')

def register_user(request):
    return render(request, 'signon.html')

def add_account(request):
    form = AccountForm(request.POST or None)
    account_list = Account.objects.all()

    context = {
        "form": form,
        "account_list": account_list
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # account.save()
            # context["created"] = True
            return redirect('moneypyle:accounts')
    else:
        return render(request, 'accounts/list.html',context=context)

def account_details(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    details = AccountEntry.objects.values().filter(account_id=account_id)
    d_dict = details.values()

    if d_dict.count() == 0:
        table = '<h2>No Data</h2>'
    else:
        df = pd.DataFrame(d_dict)
        table = df.to_html(index=False)

    safe_table = mark_safe(table)

    context = {
        "account": account,
        "details": details,
        "table": safe_table
    }
    return render(request, 'accounts/details.html', context=context)

def new_entry(request):
    if request.method == "POST":
        form = TransactionForm(request.POST or None, prefix="trans")
        form_2 = EntryFormSet(request.POST or None, prefix="entries")
        if form.is_valid() and form_2.is_valid():
            with transaction.atomic():
                parent = form.save()
                entries = form_2.save(commit=False)
                
                for idx, entry in enumerate(entries, start=1):
                    entry.transaction = parent
                    entry.line_number = idx
                    entry.save()

                print(parent, form_2)
            return redirect("moneypyle:journal")
        context = {
        "form": form,
        "form_2": form_2
        }      
        return render( request, "transactions/journal.html", context=context)
    form = TransactionForm(prefix="trans")
    formset = EntryFormSet(prefix="entries")
    context = {
        "form": form,
        "form_2": formset,
    }
    return render(request, "transactions/journal.html", context)