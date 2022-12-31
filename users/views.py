from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from .forms import UserAddForm
from .decorators import user_only, not_auth_user
from .models import ScrapModel

# Create your views here.


def home(request):
    return render(request, "home.html")


@user_only
def index(request):
    return render(request, "user-home.html")


@not_auth_user
def signup(request):  # first get the user form from forms.py to render with signup.html
    signup_form = UserAddForm()
    if (request.method == "POST"):
        form = UserAddForm(request.POST)
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
                group = Group.objects.get(name="users")
                new_user.groups.add(group)
                messages.info(request, "User Created")
                return redirect("signin")
        else:
            messages.info(
                request, "Fom validation Failed!!! Try a defferent password.")

    return render(request, "signup.html", {"signup_form": signup_form})


# @not_auth_user
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["username"] = username
            request.session["password"] = password
            login(request, user)
            print("user ------------", request.user.id)
            return redirect("index")
        else:
            messages.info(request, "Username or password incorrect ")
            return redirect("signin")
    return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect("signin")


def sc_select(request):
    return render(request, "scrap_selecter.html")


def user_pro(request):
    return render(request, "userprofile.html")


@user_only
def user_con(request, items):
    print(items.replace("%", " "))
    items = items.replace("%", " ")
    user = request.user.id
    print(user)
    # s = ScrapModel.objects.create(user=user.id, scrap_type=items)
    # s.save()
    # return render(request, "s_confirm.html")
