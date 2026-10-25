
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your FoodBridge AI account was created successfully. You can now log in.",
            )
            return redirect("login")
    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )
