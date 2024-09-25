from django import forms
from django.db import models
from .models import Teacher, CustomUser, CustomAdmin

class TutorCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subject_combination', 'first_name', 'last_name', 'email', 'phone']


class TutorLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomAdminForm(forms.ModelForm):
    class Meta:
        model = CustomAdmin
        fields = ['first_name', 'last_name', 'phone', 'username', 'admin_level']

    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['username'],
            password='defaultpassword'  # You might want to handle password more securely
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        custom_admin = super().save(commit=False)
        custom_admin.user = user
        if commit:
            custom_admin.save()
        return custom_admin
