from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . managers import CustomUserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    class Meta:
        verbose_name_plural = 'Users Admin'
        
    def __str__(self):
        return self.email