from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import venderAddForm
# from .decorators import user_only, not_auth_user

# Create your views here.


def vendor_home(request):
    return render(request, "vendor_home.html")

# @not_auth_user


def vendersign_up(request):  # first get the user form from forms.py to render with signup.html
    signup_form = venderAddForm()
    print(signup_form)
    if (request.method == "POST"):
        form = venderAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken !!! Retry")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken !!! Retry")
                return redirect("signup")
            else:
                new_user = form.save()
                new_user.save()
                group = Group.objects.get(name="venders")
                new_user.groups.add(group)
                messages.info(request, "User Created")
                return redirect("vendor_home")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "ven_signup.html", {"signup_form": signup_form})


# @not_auth_user
def vendersign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            return redirect("vendor_home")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("vendersign_in")
    return render(request, "ven_signin.html")


def signout(request):
    logout(request)
    return redirect("vendersign_in")
