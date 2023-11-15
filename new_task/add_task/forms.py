from django import forms
from .models import MyTask
from user_interface.models import MyUser

class DateInput(forms.DateInput):
    input_type = 'date'

class MyForm(forms.ModelForm):
    

    class Meta:
        model = MyTask
        fields = ['title', 'description', 'date', 'status', 'user']
        widgets ={
            'date': DateInput,
        }
