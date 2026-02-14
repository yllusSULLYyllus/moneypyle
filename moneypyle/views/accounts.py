from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
import pandas as pd

from ..models import Account, AccountEntry
from ..forms import AccountForm

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