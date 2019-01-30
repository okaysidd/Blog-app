from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import time


# Create your views here.
@login_required
def about(request):
    return render(request, 'system_app/about.html', context={'title': 'About'})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # print('Printing now - {}'.format(type(request.user)))
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('users:view-profile', kwargs={'pk':user.pk}))
                return HttpResponseRedirect(reverse('blogs:all-post'))
            else:
                return HttpResponse("<h2>This user is not active</h2>")
        else:
            return HttpResponse("<h2>Invalid username/password</h2>")

    return render(request, 'system_app/login.html', context={'title': 'Login'})


@login_required
def user_logout(request):
    logout(request)
    # time.sleep(1)
    # return HttpResponseRedirect(reverse('system:login'))
    return render(request, 'system_app/logout.html', context={'title': 'Logout'})


@login_required
def contact(request):
    return render(request, 'system_app/contact.html', context={'title': 'Contact'})
