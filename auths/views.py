from django.shortcuts import render, redirect
from .forms import CreateUserForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

# Login Function
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context={'form': form}

    return render(request, 'register.html', context)

# Logout Function

# def logout_view(request):
#     logout(request)
#     return redirect('login')
    


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render('login.html', {'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form': form})