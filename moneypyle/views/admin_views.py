from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def signon(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "Invalid Login Information"
            }
            return render(request, 'signon.html', context=context)
        login(request, user)
        return redirect('moneypyle:home')

    return render(request, 'signon.html')

def signoff(request):   
    return render(request, 'signon.html')

def register_user(request):
    return render(request, 'signon.html')

def admin_home(request):
    return render(request, 'home.html')

def clock_time(request):
    return render( request, 'clock-time.html')