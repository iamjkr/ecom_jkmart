from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, \
    SetPasswordForm
from django.contrib.auth.models import User

from base.models import Customer


class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))

    #field_order = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class LoginForm(forms.Form):
        username = forms.CharField(label="Enter User Name",widget=forms.TextInput(
            attrs={
                    'placeholder': 'User Name',
                    'class': 'form-control',
                    'autofocus': 'True'
                }
            )
        )
        password = forms.CharField(label="Enter Your Password",widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'class': 'form-control',
                    'autocomplete': 'current-password'
                }
            )
        )

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'autofocus': 'True', 'class': 'form-control','autocomplete': 'current-password'}))
    new_password2 = forms.CharField(label="Confirm New Password",widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'autofocus': 'True', 'class': 'form-control','autocomplete': 'current-password'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': 'True','autocomplete': 'current-password'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':"current-password", 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }



