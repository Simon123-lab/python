from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import User,Order,Review,ContestEntries

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','Is_worker', 'Is_client']
        
class AddOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['url','category','quantity','id_name','phone_no','img']
        
class AddReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['details','rating']
        
class ContestSubmitionForm(forms.ModelForm):
    
    class Meta:
        model = ContestEntries
        fields = ['whatsapp','facebook','twitter']