from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import User_form, Profile_form
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from .models import Author_model
from blogs_app.models import Post_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.
def profile(request):
    user_form = User_form()
    profile_form = Profile_form()

    if request.method == "POST":
        user_form = User_form(request.POST)
        profile_form = Profile_form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # done to prevent collisions since this is the same user as the user_form above
            profile = profile_form.save(commit=False)
            profile.author_name = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            return HttpResponseRedirect(reverse('system:login'))
        else:
            print(user_form.errors, profile_form.errors)
            return HttpResponse("Invalid value(s) entered")

    if request.user.is_authenticated:
        title = 'Update your profile'
    else:
        title = 'Create a profile with us'

    context = {
        'title': title,
        'user_form': user_form,
        'profile_form': profile_form,
        }
    return render(request, 'users_app/create_profile.html', context=context)


class DetailProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'users_app/profile.html'

    context_object_name = 'view_profile'
    model = Author_model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Author_model.objects.filter(author_name=get_object_or_404(User, id=self.kwargs['pk']))[0]
        posts_by_author = Post_model.objects.filter(author=profile)
        context['posts_by_author'] = posts_by_author
        context['title'] = profile
        return context

@login_required
def updateProfile(request):
    user_form = User_form()
    profile_form = Profile_form()
    display_user = User.objects.filter(username=request.user.username)[0]
    display_profile = Author_model.objects.filter(author_name=get_object_or_404(User, username=request.user.username))[0]

    if request.method == "POST":
        user_form = User_form(request.POST)
        profile_form = Profile_form(request.POST)

        first_name = request.POST.get('first_name')
        display_user.first_name = first_name

        last_name = request.POST.get('last_name')
        display_user.last_name = last_name

        display_user.save()

        git = request.POST.get('git')
        display_profile.git = git

        if 'profile_pic' in request.FILES:
            display_profile.profile_pic = request.FILES['profile_pic']

        display_profile.save()

        return HttpResponseRedirect(reverse('users:view-profile', kwargs={'pk': display_user.pk}))

    context = {
            'title': 'Edit Profile',
            'user_form': user_form,
            'profile_form': profile_form,
            'display_user': display_user,
            'display_profile' :display_profile,
            }

    return render(request, 'users_app/update_profile.html', context=context)
