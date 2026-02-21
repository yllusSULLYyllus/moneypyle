from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from ..models import Party
from ..forms import AddPartyForm



def get_headers(query) -> list:
    try:
        first = dict(query.values().first())
        print(first)
        headers = [h for h in first.keys() if h != 'id']
        return headers
    except Exception as exc:
        print(f"{exc} for Parties in get_headers function")
        return []



def party_home(request):
    active_parties = Party.objects.filter(is_active=True)
    inactive_parties = Party.objects.filter(is_active=False)
    headers = get_headers(active_parties)
    form = AddPartyForm(request.POST or None, prefix='party')
    print(active_parties)
    context = {
        "party_list": active_parties,
        "inactive": inactive_parties,
        "form": form,
        "headers": headers
    }
    if request.method == "POST":
        if 'create-party' in request.POST:
            if form.is_valid():
                form.save()
                # account.save()
                context["created"] = True
                return redirect('moneypyle:party')
        if 'update-party' in request.POST:
            try:
                print(request.POST)
                ids_to_delete = request.POST.getlist('delete_ids')
                del_parties = Party.objects.filter(id__in=ids_to_delete)
                ids_to_update = request.POST.getlist('inactive_ids')
                ia_parties = Party.objects.filter(id__in=ids_to_update)
                del_parties.update(is_active=False)
                ia_parties.update(is_active=True)
                messages.success(request, f"Inactivated {del_parties} party(ies).")
                return redirect('moneypyle:party')
            except IntegrityError as e:

                messages.error(request, "could not delete the selected parties")
    else:
        return render(request, 'parties/home.html',context=context)
    
    return render(request, 'parties/home.html', context=context)