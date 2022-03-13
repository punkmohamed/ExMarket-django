from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , first_name,last_name, username,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
             email= self.normalize_email(email),
             username = username,
             first_name= first_name,
             last_name= last_name,

        )
        # user.staff=is_staff
        # user.admin=is_admin
        # user.active=is_active
        user.set_password(password)

        user.save(using=self._db)
        return user
    # def create_staffuser(self, email, password=None):
    #
    #     user = self.create_user(
    #         email,
    #         password=password,
    #         is_staff=True
    #      #     username = username,
    #      # first_name= first_name,
    #      # last_name= last_name
    #     )
    #     #user.save(using=self._db)
    #     return user
    # #def create_superuser(self, email, password=None):
    def create_superuser(self , first_name,last_name, username,email,password):
        user = self.create_user(
            email= self.normalize_email(email),
            username = username,
            password= password,
            first_name= first_name,
            last_name= last_name,
                 #is_staff=True,
                 #is_admin = True
                # is_active = True,
                #  is_superadmin = True
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class  Account(AbstractBaseUser):

    email = models.EmailField(max_length =255,unique=True)
    first_name      = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    username      = models.CharField(max_length=50, unique=True)
    email           =models.EmailField(max_length=80,unique=True)
    phone_number      = models.CharField(max_length=50)

    #full_name= models.EmailField(max_length =255,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    #confirm= models.BoooleanField(default=False)
    #confirm_date= models.BoooleanField(default=False)



    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    objects= UserManager()

    def __str__(self):
       return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True

    # @property
    # def is_staff(self):
    #     return self.staff
    # @property
    # def is_admin(self):
    #     return self.admin
    # @property
    # def is_active(self):
    #         return self.active
# class profile(models.Model):
#     user- models.OneToneField(User)
# class GuestEmail(models.Model):
#       email= models.EmailField()
#       active = models.BooleanField(default=True)
#       update=models.DateTimeField(auto_now=True)
#       timestamp=models.DateTimeField(auto_now_add=True)
#
#       def __str__(self):
#           return self.email
