from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic  import CreateView
from .models import Comment_model, Post_model
from users_app.models import Author_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def createComment(request, pk):
    if request.method == "POST":
        comment_text = request.POST.get('comment-bar')
        post = Post_model.objects.filter(id=pk)[0]
        author = Author_model.objects.filter(author_name=request.user)[0]
        comment = Comment_model(
                            comment_text = comment_text,
                            author = author,
                            post = post,
                            )

        comment.save()

    return HttpResponseRedirect(reverse('blogs:post', kwargs={'pk': pk}))
