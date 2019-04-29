from django.db import models
from django.conf import settings

#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _

############ validators ############
from django.core.validators import FileExtensionValidator

############ django signal ############
from django.db.models.signals import post_save
from django.dispatch import receiver


############ import datetime ###########
from datetime import datetime, timedelta


########### import choices ########
from Accounts.choices import *

from django.core.validators import MaxValueValidator, MinValueValidator



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):

    username = None
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField( _('first name'), max_length=250)
    last_name = models.CharField(_('last name'), max_length=250)
    user_type = models.CharField(max_length=20, choices=User_Type, default='Admin')
    email_confirmed = models.BooleanField(default = False)
    agree = models.BooleanField(default= True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserManager()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class UserProfile(models.Model):
    """
    This model is to save user profile details
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='ProfileImage')
    industry = models.CharField(max_length= 200,choices=Industry_Choices)
    company_name = models.CharField(max_length=200)
    #company_size = models.CharField(max_length=200,choices=Company_Size_Choices)
    #address = models.TextField()
    #state = models.CharField(max_length=50)
    city = models.CharField(max_length = 50)
    postcode = models.CharField(max_length = 50)
    country = models.CharField(max_length= 50,choices=Country_Choices)
    company_logo = models.ImageField()
    company_type = models.CharField(max_length = 50,choices = Company_Type)
    contact_no = models.CharField(max_length = 10)

    def __str__(self):
        return "%s" %(self.user)

class FeedBack(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE,null = True,blank =True)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    rating = models.IntegerField(validators=[ MinValueValidator(1), MaxValueValidator(5)])
    subject = models.CharField(max_length= 50,choices=Subject_Type)
    message = models.TextField()

#-------- contact Us ----------------#
'''class ContactUs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    country_code = models.CharField(max_length =50,choices = Country_Choice)
    mobile = models.
    subject = models.CharField(max_length=200)
    message = models.TextField()'''

## when create user create his profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type =='Employer':
            UserProfile.objects.create(user=instance, profile_pic ='ProfileImage/avtar.png')
