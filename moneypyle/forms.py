from django import forms
from .models import Account, AccountEntry, Transaction
from django.forms import inlineformset_factory


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
    # template_name = 'accounts/list.html'
        fields = [ 'name', 'number', 'account_type', 'description']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_date', 'party_id', 'reference_number', 'memo', 'total_amount']


class EntryForm(forms.ModelForm):
    class Meta:
        model = AccountEntry
        fields = ['account', 'debit_amount', 'credit_amount', 'transaction_description']
    # template_name = "transactions/journal.html"

EntryFormSet = inlineformset_factory(
    parent_model=Transaction,
    model=AccountEntry,
    form=EntryForm,
    extra=1,               # number of empty forms shown initially
    can_delete=False,      # set True if you want a “delete” checkbox per row
    min_num=1,            # optional: enforce at least one entry
    validate_min=True,
)