from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        # user.save(using=self._db)
        user.save(using='User_info')
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using='User_info')
        return user
    


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(verbose_name='氏名', max_length=100, default='')
    age = models.IntegerField(verbose_name='年齢', default=0)
    address = models.CharField(verbose_name='住所', max_length=255, default='') 
    hobby = models.CharField(verbose_name='趣味', max_length=255, default='')
    job = models.CharField(verbose_name='業種', max_length=100, default='')
    job_history = models.CharField(verbose_name='職歴', max_length=255, default='')
    skill = models.CharField(verbose_name='資格', max_length=255, default='')
    post = models.CharField(verbose_name='役職', max_length=100, default='')
    mail = models.EmailField(verbose_name='メールアドレス', default='')
    phone_num = models.CharField(verbose_name='電話番号', max_length=20, default='')
    create_at = models.DateTimeField(default=timezone.now) #作成日
    update_at = models.DateTimeField(auto_now=True) #更新日
    memo = models.CharField(max_length=1000, default='')
    
    class Meta:
        db_table = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:user_login')
