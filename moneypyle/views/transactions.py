from django.shortcuts import render, redirect
from django.db import transaction
from ..forms import TransactionForm, EntryFormSet



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