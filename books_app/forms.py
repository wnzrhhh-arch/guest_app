from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GuestRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    email = forms.EmailField(max_length=254, required=True, label="Email Address")

    class Meta(UserCreationForm.Meta):
        model = User
        # This keeps the username and password, but adds the names and email
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
