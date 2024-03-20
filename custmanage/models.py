from django.db import models
from accounts.models import Users

# Create your models here.
# class UserInfo(models.Model):
#     user = models.OneToOneField(
#         User_info,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         default=None
#     )
#     name = models.CharField(verbose_name='氏名', max_length=100)
#     age = models.IntegerField(verbose_name='年齢', default=0)
#     address = models.CharField(verbose_name='住所', max_length=255) 
#     hobby = models.CharField(verbose_name='趣味', max_length=255)
#     job = models.CharField(verbose_name='業種', max_length=100)
#     job_history = models.CharField(verbose_name='職歴', max_length=255)
#     skill = models.CharField(verbose_name='資格', max_length=255)
#     post = models.CharField(verbose_name='役職', max_length=100)
#     mail = models.EmailField(verbose_name='メールアドレス')
#     phone_num = models.CharField(verbose_name='電話番号', max_length=20)
#     create_at = models.DateTimeField(auto_now_add=True) #作成日
#     update_at = models.DateTimeField(auto_now=True) #更新日
#     memo = models.CharField(max_length=1000)
    
#     class Meta:
#         db_table = 'User_info'
        
#     def __str__(self):
#         return  self.name 
    

class CustInfo(models.Model):
    user = models.ForeignKey(
        Users , on_delete=models.CASCADE
    )
    # cust = models.OneToOneField(
    #     User_info,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )

    Cust_name = models.CharField(verbose_name='氏名', max_length=100)
    Company = models.CharField(verbose_name='会社名', max_length=255)
    Cust_mail = models.EmailField(verbose_name='メールアドレス', default='')
    Company_address = models.CharField(verbose_name='会社住所', max_length=255, default='')
    Cust_post = models.CharField(verbose_name='役職', max_length=100, default='')
    Cust_job = models.CharField(verbose_name='業種', max_length=100, default='')
    Cust_skill = models.CharField(verbose_name='資格', max_length=255, default='')
    Cust_phone_num = models.CharField(verbose_name='電話番号', max_length=20, default='')
    create_at = models.DateTimeField(auto_now_add=True) #作成日
    update_at = models.DateTimeField(auto_now=True) #更新日
    importance_level = models.IntegerField(verbose_name='重要度', default=0)
    memo = models.CharField(max_length=1000, default='')

   
    class Meta:
       db_table = 'Cust_info'
       
    def __str__(self):
        return  self.Cust_name 