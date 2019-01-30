from django import forms
from django.contrib.auth.models import User
from .models import Author_model


class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        """
        args and kwargs are required while overriding the __init__ method
        so that later the user_form(request.POST) does not get an error for
        'TypeError: __init__() takes 1 positional argument but 2 were given'
        """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'register_form'

        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].widget.attrs['class'] = 'register_form'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'register_form'

        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['email'].widget.attrs['class'] = 'register_form'

        self.fields['password'].widget.attrs['placeholder'] = 'Enter a strong password'
        self.fields['password'].widget.attrs['class'] = 'register_form'


    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class Profile_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        args and kwargs are required while overriding the __init__ method
        so that later the profile_form(request.POST) does not get an error for
        'TypeError: __init__() takes 1 positional argument but 2 were given'
        """
        super().__init__(*args, **kwargs)
        self.fields['git'].widget.attrs['placeholder'] = 'Your Github profile'
        self.fields['git'].widget.attrs['class'] = 'register_form'

        self.fields['profile_pic'].widget.attrs['class'] = 'register_form'


    class Meta():
        model = Author_model
        fields = ('git', 'profile_pic')
