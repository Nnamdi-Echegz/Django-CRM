from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful !")
            return redirect('home')
        else:
            messages.success(request, "We encountered an error logging you in, please ensure your details are correct")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

#def login_user(request):
    #pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out of this application")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})