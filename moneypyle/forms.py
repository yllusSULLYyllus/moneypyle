from django import forms
from .models import Account, AccountEntry, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
    # template_name = 'accounts/list.html'
        fields = [ 'name', 'number', 'account_type', 'description']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_date', 'reference_number', 'memo']


class EntryForm(forms.ModelForm):
    class Meta:
        model = AccountEntry
        fields = ['account_id', 'credit_amount']
    # template_name = "transactions/journal.html"