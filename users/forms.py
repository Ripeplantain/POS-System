from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser as User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','phone_number', 'email','first_name','last_name','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email','first_name','last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'