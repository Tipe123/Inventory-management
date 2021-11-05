from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm , UserUpadateForm , ProfileUpdateForm
from user import forms
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}')
            return redirect('account:login')
    else:
        form = CreateUserForm()
    
    context = {
        'form':form
    }

    return render(request,'user/register.html' ,context)


def profile(request):
    return render(request , 'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpadateForm(request.POST , instance=request.user)
        profile_form = ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('account:profile')

    else:
        user_form = UserUpadateForm( instance=request.user)
        profile_form =  ProfileUpdateForm( instance = request.user.profile)
    context = { 
        'user_form':user_form,
        'profile_form':profile_form,
    }

    return render(request , "user/profile_update.html", context)