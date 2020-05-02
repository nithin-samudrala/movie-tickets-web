from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method == 'POST':
        r_form=UserRegisterForm(request.POST)
        #n_form=UserPhoneNoRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            #n_form.save()
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