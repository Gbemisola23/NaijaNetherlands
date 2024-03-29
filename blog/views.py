from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import (UpdateView)
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    renders the postview
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Renders the postdetail view
    """

    def get(self, request, slug, commentId=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        commentForm = CommentForm()
        if commentId:
            comment = Comment.objects.filter(pk=commentId).first()
            if (comment and comment.email == request.user.email):
                commentForm = CommentForm(instance=comment)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": commentForm
            },
        )

    def post(self, request, slug, commentId=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        if commentId:
            comment = get_object_or_404(
                comments, pk=commentId, email=request.user.email)
            comment_form = CommentForm(
                request.POST, request.FILES, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, 'Comment has been updated.')
                return HttpResponseRedirect(
                    reverse('post_detail', args=[slug]))
        else:
            comment_form = CommentForm(data=request.POST)
            commented = False
            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                commented = True

            return render(
                request,
                "post_detail.html",
                {
                    "post": post,
                    "comments": comments,
                    "commented": commented,
                    "comment_form": CommentForm(),
                    "liked": liked
                },
            )


class DeleteComment(View):
    """
    Renders the delete dropdown button
    """

    def get(self, request, commentId, slug, *args, **kwargs):
        comment = Comment.objects.filter(pk=commentId).first()
        if (comment and comment.email == request.user.email):
            comment.delete()
            messages.error(request, 'Comment has been deleted.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):
    """
    Render the like button
    """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def about(request):
    """
    Render the about page
    """
    return render(request, "about.html")


def contactus(request):
    """
    Render the contact page
    """
    return render(request, "contact_us.html")
