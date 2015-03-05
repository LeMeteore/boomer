from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Note(models.Model):
    # always reference the User class using setting conf
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.IntegerField(max_length=255)
    def __str__(self):
        return "your note is %s" % self.value

# custom User class to use
# based on the AbstractUser class
# works only in the begining,
# before the very first django migration
class MyUser(AbstractUser):
    is_developer = True
