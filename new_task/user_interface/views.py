from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import UserForm
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from user_interface.forms import UserForm
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from django.db.models import Q




def user_home(request):
    query = request.GET.get('q')
    users = MyUser.objects.filter(username=request.user.username)

    if query:
        users = MyUser.objects.filter(
            Q(firstname__icontains=query) | Q(phonenumber__icontains=query) | Q(email__icontains=query),
            username=request.user.username
        )
    
    return render(request, 'userhome_page.html', {'users': users})


def userform_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = MyUser.objects.create_user(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                dob=form.cleaned_data['dob'],
                gender=form.cleaned_data['gender'],
                address=form.cleaned_data['address'],
                password=form.cleaned_data['password'],
                photo=form.cleaned_data['photo'],
                status=form.cleaned_data['status'],
                username=form.cleaned_data['username'],
            )
            return redirect('user_home')
    else:
        form = UserForm()

    return render(request, 'userform_page.html', {'form': form})


def user_edit(request, user_id):
    user = get_object_or_404(MyUser, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():  
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']

            if password == confirmpassword:
                user = form.save()
                return redirect('user_home')
            else:
                print("You entered an incorrect password")
    else:
        form = UserForm(instance=user)

    return render(request, 'user_edit.html', {'form': form})




def user_delete(request, user_id):
    users = get_object_or_404(MyUser, pk=user_id)
    if request.method == 'POST':
        users.delete()
        return redirect('user_home')  
    
    return render(request, 'user_del.html', {'users': users})


def home_view(request):
    return render(request, 'main_home.html')


@csrf_protect


@login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home_view')


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'password.html', {'form': form})



