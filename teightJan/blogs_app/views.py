from django.shortcuts import render, get_object_or_404
from django.views.generic import (
                                TemplateView,
                                CreateView,
                                ListView,
                                DetailView,
                                UpdateView,
                                DeleteView,
                                )
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment_model, Post_model
from users_app.models import Author_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original', 'author']

    def form_valid(self, form):
        username=get_object_or_404(Author_model, author_name=self.request.user)
        print('username= {}'.format(username))
        author = Author_model.objects.filter(author_name=username)[0]
        print('author= {}'.format(author))
        form.instance.author = author
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a new blog'
        profile_pic = Author_model.objects.filter(author_name=self.request.user)[0].profile_pic
        context['profile_pic'] = profile_pic
        return context


class ListPostView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original', 'author']
    ordering = ['-created_on']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Let\'s Blog'
        return context


class DetailPostView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original', 'created_on', 'author']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author_model.objects.filter(post_model=get_object_or_404(Post_model, id=self.kwargs['pk']))[0].author_name
        context['title'] = 'Post by ' + str(author)
        profile_pic = Author_model.objects.filter(author_name=self.request.user)[0].profile_pic
        context['profile_pic'] = profile_pic
        comments = Comment_model.objects.filter(post=self.kwargs['pk']).order_by('-created_on')
        context['comments'] = comments
        # print('printing now -- {}'.format(comments))
        return context


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'blogs_app/post_model_update.html'

    model = Post_model
    fields = ['title_original', 'body_original']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update blog'
        profile_pic = Author_model.objects.filter(author_name=self.request.user)[0].profile_pic
        context['profile_pic'] = profile_pic
        return context


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'name'

    model = Post_model
    success_url = reverse_lazy('blogs:all-post')
