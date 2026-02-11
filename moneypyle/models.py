
from django.db import models

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
    description = models.CharField(max_length=250)

    class Meta:
        ordering = ['number']
