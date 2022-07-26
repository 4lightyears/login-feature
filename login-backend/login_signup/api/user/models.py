"""
author: Varun
"""

from django.db import models


class User(models.Model):
    """User model"""

    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=12, blank=True)
    session_token = models.CharField(max_length=30, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        """Additional settings"""

        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
