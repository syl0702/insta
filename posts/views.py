from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        pass
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)
