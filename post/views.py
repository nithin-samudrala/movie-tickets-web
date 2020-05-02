from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from .filters import PostFilter

class PostListView(ListView):
    model= Post
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=1

    def get_context_data(self,**kwarags):
        context = super().get_context_data(**kwarags)
        context['filter']= PostFilter(self.request.GET,queryset=self.get_queryset())
        return context

class PostDetailView(DetailView):
    model = Post
    context_object_name='post'

class UserPostListView(ListView):
    model = Post
    template_name='post/user_post.html'
    context_object_name='posts'
    paginate_by=1
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(seller=user).order_by('-date_posted')
    def get_context_data(self,**kwarags):
        context = super().get_context_data(**kwarags)
        context['filter']= PostFilter(self.request.GET,queryset=self.get_queryset())
        return context

class MoviePostListView(ListView):
    model= Post
    template_name='post/movie_post.html'
    context_object_name='posts'
    paginate_by=1
    def get_queryset(self):
        movie=get_object_or_404(Post,movie=self.kwargs.get('movie'))
        return Post.objects.filter(movie=movie).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields=['movie','release_date','show_date','tickets','seatNo','theater','district','theater_location','cast','language','movie_type']

    def form_valid(self,form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    fields=['movie','release_date','show_date','tickets','seatNo','theater','district','theater_location','cast','language','movie_type']

    def form_valid(self,form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.seller:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url= '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.seller:
            return True
        return False

