
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        PROVIDER = "PROVIDER", "Food Provider"
        NGO = "NGO", "NGO / Recipient Organisation"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.PROVIDER,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

