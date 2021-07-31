from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post, 'comment_form': CommentForm})


@login_required
def post_drafts(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-id')
    return render(request, 'blog/list.html', {'posts': posts})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('dashboard')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    messages.success(request, 'Comment successfully published.')
    return redirect('post_detail', pk=post.pk)


def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Comment successfully saved.')
        return redirect('post_detail', pk=post.pk)


@login_required
def comment_delete(request, pk, fk):
    post = get_object_or_404(Post, pk=fk)
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    messages.success(request, 'Comment successfully deleted.')
    return redirect('post_detail', pk=post.pk)


@login_required
def comment_approve(request, pk, fk):
    post = get_object_or_404(Post, pk=fk)
    comment = get_object_or_404(Comment, pk=pk)
    comment.approved_comment = True
    comment.save()
    messages.success(request, 'Comment successfully approved.')
    return redirect('post_detail', pk=post.pk)

