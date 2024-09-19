from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from production.views import get_summaries
from production.models import *
import json
from django.utils import timezone
from django.db.models import Sum
from production.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from .utils import get_gold_price
from production.forms import *


# Create your views here.

def create_user(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user-list')  # Redirect to a list of users or another view
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'auth/create_user.html', context)

def gold_price_view(request):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    gold_price = get_gold_price(api_key)
    context = {'gold_price': gold_price}
    return render(request, 'gold_price.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logout(request):
	auth.logout(request)
	messages.success(request, 'Your are now logged out')
	return redirect('login')