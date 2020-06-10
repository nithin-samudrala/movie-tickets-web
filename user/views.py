from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method == 'POST':
        r_form=UserRegisterForm(request.POST)
        #n_form=UserPhoneNoRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            #n_form.save()
            mail=r_form.cleaned_data['email']
            send_mail('Welcome to TMovies', """In most of current day online movie tickets booking platforms there is no provision for ticket cancellation. 
                        So if a user want to cancel his ticket he need to bare a nominal fee. 
                        To overcome this problem we made a online platform where the user has a flexibility to sell his ticket instead of cancelling.This website will be advantageous to the people who want to cancel their tickets for some emergency reasons. 
                        As our platform is  fair and transparent, both the ticket seller and the buyer will be benefited. \n In case of any service related query, please call  # 8977116440(Mon - Sat 9:30AM to 6:00PM IST)
                        or write to samudralanithin@gmail.com""",
                        settings.EMAIL_HOST_USER,[mail],fail_silently=False)
            messages.success(request,f'Your account has been created \n You can now login')
            return redirect('login')
        
    else:
        r_form=UserRegisterForm()
        
    return render(request,'user/register.html',{'r_form': r_form})

@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'user/profile.html',context) 


