from django import forms

class SignUpForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=14)
    address = forms.CharField(widget=forms.Textarea)
    preferred_tutor_gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=False)
    parent_guardian_info = forms.CharField(widget=forms.Textarea, required=False)
