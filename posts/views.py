from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
	posts=Post.objects.order_by('-pdate')
	return render(request, 'posts/home.html', {'all_posts':posts})

def showpost(request, postid):
	req_post=get_object_or_404(Post, pk=postid)
	return render(request, 'posts/fullpost.html', {'post':req_post})