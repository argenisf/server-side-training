from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mixpanel import Mixpanel
import datetime

from images.forms import SignUpForm
from images.forms import LoginForm

mp = Mixpanel("f8bd7cddaf94642530004c3d0509691f")

def index(request):
    """Return the logged in page, or the logged out page
    """
    print('Index view!')
    if request.user.is_authenticated():
        return render(request, 'images/index-logged-in.html', {
            'user': request.user,
            'email': request.user.email
        })
    else:
        return render(request, 'images/index-logged-out.html')


def signup(request):
    """Render the Signup form or a process a signup
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            
            mp_distinct_id = request.POST['mp_did']
            now = datetime.datetime.utcnow()
            
            mp.track(mp_distinct_id, "Signup",{
                "Username": username,
                "Signup Date": now.strftime("%Y-%m-%dT%H:%M:%S")
            });

            mp.alias(email, mp_distinct_id)

            user = authenticate(username=username, password=raw_password)
            log_in(request, user)
            return HttpResponseRedirect('/')

    else:
        form = SignUpForm()

    return render(request, 'images/signup.html', {'form': form})


def login(request):
    """Render the login form or log in the user
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            log_in(request, user)

            mp.track(request.user.email, "Login");

            return HttpResponseRedirect('/')
        else:
            return render(request, 'images/login.html', {
                'form': LoginForm,
                'error': 'Please try again'
            })
    else:
        return render(request, 'images/login.html', {'form': LoginForm})



def logout(request):
    """Logout the user
    """
    log_out(request)
    return HttpResponseRedirect('/')
