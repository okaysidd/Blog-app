from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
                                TemplateView,
                                CreateView,
                                ListView,
                                DetailView,
                                UpdateView,
                                DeleteView,
                                TemplateView,
                                )
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment_model, Post_model
from users_app.models import Author_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.utils import timezone


# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original']

    def form_valid(self, form):
        username=get_object_or_404(Author_model, author_name=self.request.user)
        # print('username= {}'.format(username))
        if Author_model.objects.filter(author_name=username):
            if Author_model.objects.filter(author_name=username)[0]:
                author = Author_model.objects.filter(author_name=username)[0]
                form.instance.author = author
        # print('author= {}'.format(author))
        # form.instance.created_on = timezone.now()
        # form.instance.modified_on = timezone.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a new blog'
        if Author_model.objects.filter(author_name=self.request.user):
            if Author_model.objects.filter(author_name=self.request.user)[0]:
                profile_pic = Author_model.objects.filter(author_name=self.request.user)[0].profile_pic
                context['profile_pic'] = profile_pic
        return context


class ListPostView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original', 'author']

    # ordering = ['-created_on']
    # ordering = ['-modified_on']
    ordering = ['-published_on']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Let\'s Blog'
        return context


class DetailPostView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    fields = ['title_original', 'body_original', 'created_on', 'author', 'published_on', 'title_edited', 'body_edited']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author_model.objects.filter(post_model=get_object_or_404(Post_model, id=self.kwargs['pk']))[0].author_name
        context['title'] = 'Post by ' + str(author)
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

    def form_valid(self, form):
        if form.instance.published_on:
            if not form.instance.modified_on:
                form.instance.title_edited = Post_model.objects.filter(pk=self.kwargs['pk'])[0].title_original
                form.instance.title_original = str(form.instance.title_original) + "(edited)"
                form.instance.body_edited = Post_model.objects.filter(pk=self.kwargs['pk'])[0].body_original
                # if not str(form.instance.title_original).endswith('(edited)'):
            form.instance.modified_on = timezone.now()
        # print('-------print------- {}'.format(type(form.changed_data[0])))
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'name'

    model = Post_model
    success_url = reverse_lazy('blogs:all-post')


def publish_post(request, pk):
    post = get_object_or_404(Post_model, pk=pk)
    post.publish()
    return redirect('blogs:post', pk=pk)


class DetailPostHistoryView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'next'

    model = Post_model
    template_name = 'blogs_app/post_history.html'
    fields = ['title_original', 'body_original', 'created_on', 'author', 'published_on', 'title_edited', 'body_edited']

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


def searchResults(request):
    search_query = ""
    authors = ""
    authors_git = ""
    posts_title = ""
    posts_body = ""

    if request.method == "POST":
        if request.POST.get('search-query'):
            search_query = request.POST.get('search-query')
            if search_query:
                authors = Author_model.objects.filter(author_name__username__icontains=search_query)
                authors_git = Author_model.objects.filter(git__icontains=search_query)

                posts_title = Post_model.objects.filter(title_original__icontains=search_query)
                posts_body = Post_model.objects.filter(body_original__icontains=search_query)
    context = {
            'title': 'Search results for '+search_query ,
            'search_query': search_query,
            'authors': authors,
            'authors_git': authors_git,
            'posts_title': posts_title,
            'posts_body': posts_body,
            }
    return render(request, 'blogs_app/search_results.html', context=context)
