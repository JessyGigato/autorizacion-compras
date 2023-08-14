from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Usuario(AbstractUser):
    #user = models.OneToOneField(User, related_name='usuario_info', null=True, blank=True, on_delete=models.CASCADE )
    rol = models.CharField(max_length=15, null=True, blank=True)
    firma = models.CharField(max_length=128, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='usuario_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='usuario_user_permissions',
        related_query_name='user',
    )

    # def set_firma(self, raw_firma):
    #     self.firma = make_password(raw_firma)
    #     self.save()

    # def check_firma(self, raw_firma):
    #     if self.firma is None:
    #         return False
    #     return check_password(raw_firma, self.firma)