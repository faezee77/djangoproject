# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, mobile_number, first_name, last_name, province, province_id, city,
                    address):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.mobile_number = mobile_number
        user.first_name = first_name
        user.last_name = last_name
        user.city = city
        user.province = province
        user.province_id = province_id
        user.address = address
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, mobile_number, first_name, last_name):
        user = self.create_user(
            username=username,
            email=email,
            mobile_number=mobile_number,
            password=password,
            first_name=first_name,
            last_name=last_name,
            city='اصفهان',
            province='اصفهان',
            province_id='13',
            address='address'

        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    mobile_number = models.CharField(max_length=50, null=True, default='09028080656')
    email = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, default='احمدی')
    province = models.CharField(max_length=50, null=True, default='اصفهان')
    province_id = models.CharField(max_length=50, null=True, default='13')
    city = models.CharField(max_length=50, null=True, default='اصفهان')
    address = models.CharField(max_length=100, null=True, default='خیابان اصلی')

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'mobile_number', 'first_name', 'last_name']
    objects = AccountManager()

    def __str__(self):
        return self.username
