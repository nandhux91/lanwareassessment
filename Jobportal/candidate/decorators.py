from django.shortcuts import redirect

def sign_in_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper

def is_employer(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.role=="employer":
            return fun(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper