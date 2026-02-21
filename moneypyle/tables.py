import django_tables2 as tables
from .models import Transaction, AccountEntry

class TransactionsTable(tables.Table):
    class Meta:
        model = AccountEntry