from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import singup_from,userprofilechange,GeeksForm

    

def sing_up(request):
    form=singup_from()
    registered=False
    if(request.method=="POST"):
        form=singup_from(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
    dict={'form':form,'registered':registered} 
    return render(request,'sing_up.html',context=dict)       


def log_in(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('abc'))
    
    return render(request,'login.html',context={'form':form})

@login_required
def logout_page(request):
    logout(request)
    return  HttpResponseRedirect(reverse('abc'))

@login_required
def profile_view(request):
    return render(request,'profile.html',context={})


@login_required
def user_change(request):
    current_user=request.user
    form=userprofilechange(instance=current_user)
    if request.method=='POST':
        form=userprofilechange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form=userprofilechange(instance=current_user)
    return render(request,'changeprofile.html',context={'form':form})        

@login_required
def password_change(request):
    current_user=request.user
    form=PasswordChangeForm(current_user)
    if request.method=='POST':
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()

    return render(request,'change_password.html',context={'form':form})



@login_required
def add_pro_pic(request):
    form=GeeksForm()
    if request.method=='POST':
        form=GeeksForm(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.User=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('profile'))
    return render (request,'pro_pic.html',context={'form':form})


@login_required
def change_pro_pic(request):
    form=GeeksForm(instance=request.user.user_profile)
    if request.method=="POST":
        form=GeeksForm(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))

    return render(request,'pro_pic.html',context={'form':form})
