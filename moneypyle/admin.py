from django.contrib import admin
from .models import Account, AccountEntry, Party, Product, Company, Transaction

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
@admin.register(AccountEntry)
class AccountEntryAdmin(admin.ModelAdmin):
    pass

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_date', 'party_id', 'reference_number', "total_amount", 'memo')