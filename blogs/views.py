from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# def home(request):
#     return render(request, 'home-page.html', {})

# def checkout(request):
#     return render(request, 'checkout-page.html', {})

# def product(request):
#     return render (request, 'product-page.html', {})


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_listview.html'



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detailview.html'
    

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['name','body']

