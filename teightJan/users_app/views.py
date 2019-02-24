from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .forms import User_form, Profile_form
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from .models import Author_model
from blogs_app.models import Post_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone


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
        if Author_model.objects.filter(author_name=get_object_or_404(User, id=self.kwargs['pk'])):
            profile = Author_model.objects.filter(author_name=get_object_or_404(User, id=self.kwargs['pk']))[0]
            posts_to_publish = Post_model.objects.filter(author=profile, published_on=None)
            posts_by_author = Post_model.objects.filter(author=profile, published_on__lte=timezone.now())
            context['posts_by_author'] = posts_by_author
            context['posts_to_publish'] = posts_to_publish
        else:
            context['profile'] = 'not found'
        context['title'] = profile
        return context


def profileView(request, pk):
    context = {}
    if Author_model.objects.filter(author_name=get_object_or_404(User, id=pk)):
        profile = Author_model.objects.filter(author_name=get_object_or_404(User, id=pk))[0]
        posts_to_publish = Post_model.objects.filter(author=profile, published_on=None)
        posts_by_author = Post_model.objects.filter(author=profile, published_on__lte=timezone.now())
        if Author_model.objects.filter(author_name=request.user):
            if profile in Author_model.objects.filter(author_name=request.user)[0].following.all():
                followed = True
            else:
                followed = False
        else:
            followed = False
        context['posts_by_author'] = posts_by_author
        context['posts_to_publish'] = posts_to_publish
        context['title'] = profile
        context['view_profile'] = profile
        context['followed'] = followed
        context['people_followed'] = Author_model.objects.filter(author_name=request.user)[0].following.all()
        # context['followed_by'] = Author_model.objects.filter(following=request.user).all()
        current_user = Author_model.objects.filter(author_name=request.user)[0]
        print('-----------------{}'.format(Author_model.objects.filter(following=current_user).all()))

        return render(request, 'users_app/profile.html', context=context)
    else:
        profile = User.objects.filter(username=request.user.username)[0]
        context['profile'] = profile
        return render(request, 'users_app/create_social_profile.html', context=context)



@login_required
def updateProfile(request):
    user_form = User_form()
    profile_form = Profile_form()
    display_user = User.objects.filter(username=request.user.username)[0]
    display_profile = ""
    if Author_model.objects.filter(author_name=get_object_or_404(User, username=request.user.username)):
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


def create_social_profile(request):
    user_profile = User.objects.filter(username=request.user.username)[0]
    if request.method == "POST":
        if request.POST.get('first_name'):
            user_profile.first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            user_profile.last_name = request.POST.get('last_name')

        user_profile.save()

        author = Author_model(
                            author_name = user_profile,
                            )

        if request.POST.get('git'):
            author.git = request.POST.get('git')

        if 'profile_pic' in request.FILES:
            author.profile_pic = request.FILES['profile_pic']

        author.save()

        return redirect('users:view-profile', pk=request.user.pk)


def follow_user(request, pk):
    author = Author_model.objects.filter(author_name=request.user)[0]
    followed_author = Author_model.objects.filter(author_name=pk)[0]
    author.follow_user(followed_author)
    return redirect('users:view-profile', pk=pk)
