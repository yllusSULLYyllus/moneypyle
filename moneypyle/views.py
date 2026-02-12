from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.forms.models import modelformset_factory
import pandas as pd

from .models import Account, AccountEntry
from .forms import TransactionForm, AccountForm, EntryForm

class AccountView(ListView):
    model = Account
    template_name = 'accounts/list.html'
    fields = ['name']

# class journal(CreateView):
#     model = AccountEntry
#     fields = ['account_id', 'credit_amount']
#     template_name = "transactions/journal.html"

def home(request):
    return render(request, "home.html")

def add_account(request):
    form = AccountForm
    account_list = Account.objects.all()
    context = {
        "form": form,
        "account_list": account_list
    }
    return render(request, 'accounts/list.html',context=context)

def account_details(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    print(account)
    details = AccountEntry.objects.values().filter(account_id=account_id)
    d_dict = details.values()
    df = pd.DataFrame(d_dict)
    table = df.to_html()
    from django.utils.safestring import mark_safe
    safe_table = mark_safe(table)

    context = {
        "account": account,
        "details": details,
        "table": safe_table
    }
    return render(request, 'accounts/details.html', context=context)

def new_entry(request):
    form = TransactionForm
    form_2 = EntryForm
    # obj = get_object_or_404(Account)
    # Formset = modelformset_factory()
    EntryFormset = modelformset_factory(AccountEntry, form=EntryForm, extra=0)

    # qs = obj.g
    # formset = EntryFormset(request.POST or None, queryset=)

    context = {
        "form": form,
        "form_2": form_2,
    }
    return render( request, "transactions/journal.html", context=context)