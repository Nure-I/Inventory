from django.shortcuts import render, redirect
from django.contrib import messages, auth
from account.decorators import unauthenticated_user
# Create your views here.

# @unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if request.user.groups.filter(name='sales').exists():
                return redirect('spindex')
            elif request.user.groups.filter(name='reception').exists():
                return redirect('wh1index')
            elif request.user.groups.filter(name='stock').exists():
                return redirect('wh2index')
            elif request.user.groups.filter(name='shareholder').exists():
                return redirect('shindex')
            else:
                return redirect('login')

            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'page/login.html')

def logout(request):
    
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return render(request, 'page/login.html')