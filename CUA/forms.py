from django.contrib.auth.forms import UserChangeForm ,UserCreationForm
from .models import Customer
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "is_customer",
            )
        widgets = {
            "is_customer" : forms.RadioSelect(attrs={'class':'form-check'}),
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",             
            )

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = (
            "profil_pic",
            "statut_pic",
            "age",
            "telephone",
            "is_customer",
            "username",
            "first_name",
            "last_name",
            "email", 
            )

class ProfilListForm(forms.Form):
    class Meta:
        fields = (
        "profil_pic",
        "statut_pic",
        "age",
        "telephone",
        "is_customer",
        "username",
        "first_name",
        "last_name",
        "email", 
            )