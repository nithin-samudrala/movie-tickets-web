from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from .filters import PostFilter
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings

Profile = apps.get_model('user', 'Profile')

class PostListView(ListView):
    model= Post
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=20

    def get_context_data(self,**kwarags):
        context = super().get_context_data(**kwarags)
        context['filter']= PostFilter(self.request.GET,queryset=self.get_queryset())
        return context

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name='post'
    
    def get_context_data(self,**kwarags):
        user=get_object_or_404(Post,pk=self.kwargs.get('pk'))
        #print(user.seller)
        context = super().get_context_data(**kwarags)
        #abc=get_object_or_404(Profile,user=user.seller)
        #abc=Profile.objects.filter(user=user.seller).first()
        #print(abc.phoneNo)
        context['profile']=Profile.objects.filter(user=user.seller).first()
        return context

class UserPostListView(LoginRequiredMixin,ListView):
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
    fields=['movie','release_date','show_date','cost','tickets','seatNo','theater','district','theater_location','cast','language','movie_type']

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        #initial_date={"release_date":"2020-04-29 11:31:54"}
        form.fields['release_date'].widget = forms.TextInput(attrs={'placeholder':'2020-04-29 11:31:54'})
        form.fields['show_date'].widget = forms.TextInput(attrs={'placeholder':'2020-04-29 11:31:54'})
        return form

    def form_valid(self,form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    fields=['movie','release_date','show_date','cost','tickets','seatNo','theater','district','theater_location','cast','language','movie_type']
    
    def get_form(self, form_class=None):
        form = super(PostUpdateView, self).get_form(form_class)
        #initial_date={"release_date":"2020-04-29 11:31:54"}
        form.fields['release_date'].widget = forms.TextInput(attrs={'placeholder':'2020-04-29 11:31:54'})
        #form.fields['show_date'].widget = forms.TextInput(attrs={'placeholder':'2020-04-29 11:31:54'})
        return form
    
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

@login_required
def payment(request,**kwargs):
    #intrested=request.user
    #sel=kwargs.get('pk')
    #user=get_object_or_404(Profile,user=kwargs.get('username'))
    seller=Profile.objects.filter(pk=kwargs.get('pk')).first()
    #print(seller)
    intrested=Profile.objects.filter(user=request.user).first()
    inmail=User.objects.filter(username=intrested.user).first()
    selmail=User.objects.filter(username=seller.user).first()
    #print(inmail.email)
    #print(selmail.email)
    #seller=Profile.objects.filter(user=sel)
    #print(intrested.phoneNo)
    #print(sel)
    #print(seller)
    #print(intrested.user)
    message1=('{name} is intrested in buying your ticket'.format(name=intrested.user),
                '''{name} is intrested in buying your ticket use these details to contact \n PHONE NUMBER:{phoneNO} \n
                    Email:{email}'''.format(name=intrested.user,phoneNO=intrested.phoneNo, email=inmail.email),
                    settings.EMAIL_HOST_USER,[selmail.email]
    )
    message2=('Hello {name} thanks for using Tmovies'.format(name=intrested.user),
                '''Hear are the details of the owner your looking for hear are the details of the owner:
                    Name:{name} \n PHONE NUMBER:{phoneNO} \n
                    Email:{email}'''.format(name=intrested.user,phoneNO=intrested.phoneNo, email=inmail.email),
                    settings.EMAIL_HOST_USER,[inmail.email]

    )
    send_mass_mail((message1, message2), fail_silently=False)


    return render(request,'post/payments.html')

    
