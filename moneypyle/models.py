
from decimal import Decimal
from django.db import models
from django.db.models import F
from django.db.models.functions import Concat

# Meta models

class Address(models.Model):
    class State(models.TextChoices):
        Ohio = "OH"
    street = models.CharField()
    state = models.CharField(choices=State)
    zip = models.IntegerField()
    country = models.CharField()
    class Meta():
        abstract = True

# Core Models
class Company(Address):
    company_name = models.CharField()
    description = models.CharField(blank=True)
    industry = models.CharField()

class Account(models.Model):
    ACCOUNT_TYPES = [ 
        ("AS", "Asset"),
        ("LI", "Liability"),
        ("EQ","Equity"),
        ("IN", "Income"),
        ("EX", "Expenses")
    ]

    name = models.CharField(max_length=40)
    number = models.IntegerField()
    account_type = models.CharField(choices=ACCOUNT_TYPES)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.name
    
    def list_assets(self):
        return self.account_type == "AS"

class Party(models.Model):
    party_type = models.CharField(null=True, blank=True)
    first_name = models.CharField()
    last_name = models.CharField()
    full_name = models.GeneratedField(expression=Concat('first_name', models.Value(' '), 'last_name'), output_field=models.CharField(max_length=64), db_persist=True)
    email = models.EmailField(blank=True)
    company_id = models.ManyToManyField(Company, related_name="Party", blank=True)

class Product(models.Model):
    name = models.CharField()
    type = models.CharField(blank=True)
    product_description = models.CharField(blank=True)

class Transaction(models.Model):
    logged_date = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateField()
    party_id = models.ForeignKey(Party, on_delete=models.PROTECT)
    reference_number = models.CharField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    memo = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.reference_number

class InvoiceLine(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    transaction_description = models.CharField(blank=True)
    quantity = models.IntegerField()
    rate = models.FloatField()
    line_total = models.GeneratedField(expression=F("quantity") * F("rate"), db_persist=True, output_field=models.DecimalField(decimal_places=2, max_digits=10))
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    line_number = models.IntegerField()

class AccountEntry(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit_amount = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal(0))
    credit_amount = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal(0))
    transaction_description = models.CharField(blank=True)
    line_number = models.IntegerField()
    

class Event(models.Model):
    event_date = models.DateField()
    debit_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="debit_account")
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    debit_party = models.ForeignKey(Party, on_delete=models.PROTECT, blank=True, related_name="debit_party")
    credit_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="credit_account")
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_party = models.ForeignKey(Party, on_delete=models.PROTECT, blank=True, related_name="credit_party")
    memo = models.CharField()

    def __str__(self):
        return self.memo