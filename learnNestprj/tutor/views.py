from django.views.decorators.cache import never_cache
from .models import CustomUser, CustomAdmin, Teacher
import random
import string
from .forms import TutorCreationForm
from .forms import TutorLoginForm, CustomAdminForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout

def is_admin(user):
    return user.is_staff

@login_required
def admin_dashboard(request):
    print(request.user.__dict__)
    teachers = Teacher.objects.all()
    print(teachers)
    return render(request, 'tutor/custom_admin/dashboard.html', {'teachers': teachers})


def create_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print("username, email, password")
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "User already exist pls login")
            print("User already exist")
            return redirect('admin_login')
        else:
            # User does not exist
            CustomUser.objects.create_superuser(username=username, password=password, email=email)
            try:
                custom_admin_group = Group.objects.get(name='CustomAdmin')
            except Group.DoesNotExist:
                print("Group customAdmin does not exist")

            # CustomUser.groups.add(custom_admin_group)
            CustomUser.is_staff = True
            # CustomUser.save()

            # CustomAdmin.objects.create(CustomUser=CustomUser)
            return redirect('admin_login')

    return render(request, 'tutor/create_admin.html')

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        print("authenticated")
        # return redirect("custom-admin_dashboard")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        print(user)
        print("user above")
        if user is not None:
            login(request, user)
            print(f"login request {login}")
            return redirect('custom-admin_dashboard')
        else:
            print("An error occured")
            pass
    return render(request, 'tutor/admin_login.html')

def admin_logout(request):
    print("Logging out...")
    logout(request)

    return render(request, 'tutor/admin_logout.html')

def create_tutor(request):
    if request.method == "POST":
        form = TutorCreationForm(request.POST)
        if form.is_valid():
            # generating random passwd
            password = "passwd124"
            # creating a User instance
            user = CustomUser.objects.create_user(
                    email = form.cleaned_data['email'],
                    # email = form.cleaned_data['username'],
                    password=password

                    )
            print(f"this is the default passwd: {user.password}")
            print(f"User: {user}")
            print("user created above")
            # creating teacher instance
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            print(f"Teacher: {teacher}")
            print("teacher instance created above") 
            return redirect('tutor_created')
    else:
        form = TutorCreationForm()
        return render(request, 'tutor/create_tutor.html', {'form':form})


@login_required
def tutor_created(request):
    return redirect('custom-admin_dashboard')

@never_cache
def tutor_login(request):
    if request.method == "POST":
        print(request.POST.get('csrfmiddlewaretoken'))
        form = TutorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_first_login:
                    user.is_first_login = False
                    user.save()
                    print(f"{user} is login for the first time")
                    return redirect('reset_password')
                return redirect('tutors_dashboard')
    else:
        form = TutorLoginForm()
    
    print("User is none")
    return render(request, 'tutor/tutor_login.html', {'form':form})


@login_required
def reset_password(request):
    if request.method == "POST":
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user) # Keep the user logged in
            return redirect('tutors_dashboard')

    return render(request, 'tutor/reset_password.html')

@login_required
def tutors_dashboard(request):
    return render(request, 'tutor/tutors_dashboard.html')


def custom_logout(request):
    if request.method == "POST":
        print("Post request below")
        print(request.POST.get('csrfmiddlewaretoken'))
        logout(request)
        return redirect('tutor_login')

    return redirect('tutors_dashboard')

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TeacherForm(instance=teacher)
        return render(request, 'edit_teacher.html', {'form': form})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'teacher': teacher})
