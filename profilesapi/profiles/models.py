from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Profile model class. 

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    # For the __str__ representation since the User Model itself extends from
    # an AbstractUser class. We then call the username function from that
    # class that we're linking the user to.
    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
    # ProfileStatus model class. Links to a profile through foreign key.

    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # On the admin side, by default when Django registers the plural version
    # of the model by simply adding only an 's'. In this instance it would be
    # ProfileStatuss. With the below meta class we can set it to 'statuses'
    # which is more correct.
    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return str(self.user_profile)

