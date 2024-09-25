from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from .tokens import token_generator
import smtplib
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .sign_up import SignUpForm

def homepage(request):
    return render(request, 'homepage/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['email']).exists():
                form.add_error('email', 'A user with this email already exists')
                print("A user with a similar name already exists")
                return render(request, 'homepage/sign_up.html')
            else:
                new_user = User.objects.create_user(
                        username=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        email=form.cleaned_data['email']
                        )

            # Save additional fields
            print(form.cleaned_data['phone_number'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['preferred_tutor_gender'])
            print(form.cleaned_data['parent_guardian_info'])
            new_user.is_active = True
            new_user.save()
            print("This is the new user")
            print(new_user.username, new_user.email, new_user.is_active)
            # send_confirmation_email(new_user)

            # Redirect or render a success message
            return render(request, 'homepage/notification.html')
    else:
        print("What is this...")
        form = SignUpForm()
    return render(request, 'homepage/sign_up.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        if request.POST.get('action') == 'login':
            username = request.POST['username']
            password = request.POST['password']
            print(f"Username: {username}")
            print(f"Password: {password}")
            user = authenticate(request, username=username, password=password)
            print(user)
            print("The above is the user")
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'homepage/login.html', {'error': f'Invalid details'})
        elif request.POST.get('action') == 'register':
            return redirect('sign_up')
        else:
            return render(request, 'homepage/login.html')
    return render(request, 'homepage/login.html')


def edexcel(request):
    return render(request, 'homepage/edexcel.html')

def igcse(request):
    return render(request, 'homepage/igcse.html')

def eight_four_four(request):
    return render(request, 'homepage/844.html')

def home(request):
    return render(request, 'homepage/home.html')

def user_account(request):
    return render(request, 'homepage/user_account.html')

@login_required
def dashboard(request):
    return render(request, 'homepage/index.html', {'user': request.user})
