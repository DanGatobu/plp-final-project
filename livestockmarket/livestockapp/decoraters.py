from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def group_required(group_name, redirect_url=None):
   
    def check_group(user):
        return user.groups.filter(name=group_name).exists()

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not check_group(request.user):
                if redirect_url:
                    return redirect(redirect_url)
                else:
                    return redirect('loginpage')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def unauthenticated_user(veiwfunc):
    def wraperfunc(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return veiwfunc (request,*args, **kwargs)
    
    return wraperfunc
        
