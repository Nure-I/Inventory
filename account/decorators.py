from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.groups.filter(name='sales').exists():
            print('sales')
            return redirect('spindex')
        elif request.user.groups.filter(name='reception').exists():
            print('recep')
            return redirect('wh1index')
        elif request.user.groups.filter(name='stock').exists():
            print('stock')
            return redirect('wh2index')
        elif request.user.groups.filter(name='shareholder').exists():
            print('share')
            return redirect('shindex')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.info(
                    request, "You're not Authorized to this page ")
                if request.user.groups.filter(name='sales').exists():
                    return redirect('spindex')
                elif request.user.groups.filter(name='reception').exists():
                    return redirect('wh1index')
                elif request.user.groups.filter(name='stock').exists():
                    return redirect('wh2index')
                elif request.user.groups.filter(name='shareholder').exists():
                    return redirect('shindex')

        return wrapper_func

    return decorator
