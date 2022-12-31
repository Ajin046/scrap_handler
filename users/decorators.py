from django.shortcuts import redirect


def user_only(view_func):

    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')

    return wrapper_function


def not_auth_user(view_func):

    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function
