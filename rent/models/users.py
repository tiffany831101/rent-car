from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    lisense = models.CharField(max_length=50, null=False)

    # is a legal user at first
    legal_user = models.BooleanField(default=True)

    # default does not have any violate times
    violate_times = models.IntegerField(default=0)
