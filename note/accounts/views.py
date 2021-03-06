from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserLoginForm, UserRegisterForm, ProfileForm

# Create your views here.

def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    user_form = UserRegisterForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        # profile_form.save(commit=False)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    return render(request, "accounts/join.html", {'user_form': user_form, 'profile_form': profile_form})



def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('memo_list')
            else:
                return HttpResponse('유효한 계정이 아닙니다. 다시 시도 해보세요.')

    return render(request, "accounts/login.html", {"form":form})



def logout_view(request):
    logout(request)
    return redirect("/")