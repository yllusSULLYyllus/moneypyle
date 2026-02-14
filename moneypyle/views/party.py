from django.shortcuts import render
from django.db import 
from ..models import Party

def party_home(request):
    parties = Party.objects.all()
    context = {
        "party_list": parties
    }
    return render(request, 'parties/home.html', content=context)