from django.shortcuts import render
from django.utils import timezone
from .models import Post #import each model from models.py (ex.01) 
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


from .forms import DocumentForm

def post_list(request):
    posts = Post.objects.filter()#this is a query set, it filters data out of the database and choses the criteria to sort it ex.02
    return render(request, 'blog/post_list.html', {'posts': posts})#ex03

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

