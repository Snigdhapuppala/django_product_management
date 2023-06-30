from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']  # snigdha
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username Exist..! try another name')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already taken, try another one')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')
        else:
            print("Password did not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':  # if the condition is true if enter into the if condition
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, user)
            print("Login successfully...")
            return redirect('showProducts')
        else:
            print("Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("Logout successfully...")
        return redirect('login')




