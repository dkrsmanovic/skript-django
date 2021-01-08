from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def registerPage(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('film:lista')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('film:lista')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('film:lista')