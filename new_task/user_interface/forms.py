from django import forms
from .models import MyUser
from django.forms import RadioSelect
from django.contrib.auth.forms import PasswordChangeForm

class DateInput(forms.DateInput):
    input_type = 'date'
class UserForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = MyUser
        fields = ['firstname', 'lastname', 'phonenumber', 'email', 'dob', 'gender', 'address', 'password', 'photo', 'status', 'username']
        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'firstname': 'FirstName',
            'lastname': 'LastName',
            'phonenumber': 'PhoneNumber',
            'email': 'Email',
            'dob': 'DOB',
            'gender': 'Gender',
            'address': 'Address',
            'password': 'Password',
            'confirmpassword': 'Confirm Password',
            'photo': 'Photo',
            'status': 'Status',
            'username': 'Username',
        }

        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmpassword')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class CustomPasswordChangeForm(PasswordChangeForm):
    new_password2 = forms.CharField(
        label="Confirm New password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        strip=False,
        help_text ="Enter the same password as above,for verification."
    )
  

