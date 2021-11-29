from django.shortcuts import redirect
from django.http import HttpResponse

def allowerd_users(allowerd_rules = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            for roule in allowerd_rules:
                if request.user.groups.filter(name = roule):
                    return view_func(request, *args, **kwargs)    
            return redirect('error-view')

        return wrapper_func
    return decorator


def unauthenticated_user(view_func):
    
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home-view')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func