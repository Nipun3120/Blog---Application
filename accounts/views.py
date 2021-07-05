from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def loginView(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(data = request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect('core:home')
    else:
        loginForm = AuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'loginForm': loginForm})


@login_required
def logoutView(request):
    logout(request)
    return redirect('accounts:login')



def signupView(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            print(user)
            login(request, user)
            return redirect('core:home')
    else:
        signupForm = UserCreationForm()
        return render(request, 'accounts/signup.html', {'signupForm': signupForm})


