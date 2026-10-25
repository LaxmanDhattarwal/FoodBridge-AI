
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-input",
            "placeholder": "Enter your email address",
            "autocomplete": "email",
        }),
    )

    role = forms.ChoiceField(
        choices=User.Role.choices,
        widget=forms.Select(attrs={
            "class": "form-input",
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "role",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Choose a username",
                "autocomplete": "username",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Choose a username",
            "autocomplete": "username",
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Create a strong password",
            "autocomplete": "new-password",
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Confirm your password",
            "autocomplete": "new-password",
        })
