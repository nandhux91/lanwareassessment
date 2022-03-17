from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email,name, date_of_birth,phone,role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
            phone=phone,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,date_of_birth,phone,role, password=None,):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            name=name,
            phone=phone,
            role=role
        )
        user.is_admin = False
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    name = models.CharField(max_length=100,null=True)
    options = (("employer", "employer"),
               ("candidate", "candidate"))
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=120, choices=options)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'phone', 'role']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Jobs(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    designation=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=250,null=True)
    company=models.CharField(max_length=250,null=True)
    location=models.CharField(max_length=250,null=True)
    options=(
        ("python","python"),
        ("django","django"),
        ("reactjs","react"),
        ("nodejs","nodejs"),
        ("java","java"),
        ("android","android"),
        ("others","others"))
    skills=models.CharField(max_length=200,choices=options)
    salary=models.PositiveIntegerField(null=True)
    posted_date=models.DateField(auto_now_add=True)




