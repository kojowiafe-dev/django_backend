import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User'), ('preacher', 'Preacher')], default='user')

    def __str__(self):
        return self.role
