from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import ImageField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField


# user model

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user_object(self, phone_number, password, **extra_fields):

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        return user

    def _create_user(self, phone_number, password, **extra_fields):
        user = self._create_user_object(phone_number, password, **extra_fields)
        user.save(using=self._db)
        return user

    async def _acreate_user(self, phone_number, password, **extra_fields):
        user = self._create_user_object(phone_number, password, **extra_fields)
        await user.asave(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    create_user.alters_data = True

    async def acreate_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return await self._acreate_user(phone_number, password, **extra_fields)

    acreate_user.alters_data = True

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)

    create_superuser.alters_data = True

    async def acreate_superuser(
        self, phone_number, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return await self._acreate_user(phone_number, password, **extra_fields)

    acreate_superuser.alters_data = True

class User(AbstractUser):
    class RoleType(TextChoices):
        MANAGER = 'manager' , 'Manager'
        COOK = 'cook' , 'Cook'
        ADMIN = 'admin' , 'Admin'
        PARENTS = 'parents' , 'Parents'
        DOCTOR = 'doctor' , 'Doctor'
        TEACHER = 'teacher' , 'Teacher'
        SUPERVISOR = 'supervisor' , 'Supervisor'
        USER = 'user' , 'User'

    phone_number = CharField(max_length=20 , unique=True)
    role = CharField(choices=RoleType , max_length=15)
    country_code = CharField(max_length=5)
    objects = CustomUserManager()
    avatar = ImageField(upload_to="users/" , null=True)
    email = None
    username = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
