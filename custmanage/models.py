from django.db import models
from accounts.models import Users    

class CustInfo(models.Model):
    user = models.ForeignKey(
        Users , on_delete=models.CASCADE
    )
    Cust_name = models.CharField(verbose_name='氏名', max_length=100)
    Company = models.CharField(verbose_name='会社名', max_length=255)
    Cust_mail = models.EmailField(verbose_name='メールアドレス', default='')
    Company_address = models.CharField(verbose_name='会社住所', max_length=255, default='')
    Cust_post = models.CharField(verbose_name='役職', max_length=100, default='')
    Cust_job = models.CharField(verbose_name='業種', max_length=100)
    Cust_skill = models.CharField(verbose_name='資格', max_length=255)
    Cust_phone_num = models.CharField(verbose_name='電話番号', max_length=20, default='')
    create_at = models.DateTimeField(auto_now_add=True) #作成日
    update_at = models.DateTimeField(auto_now=True) #更新日
    importance_level = models.IntegerField(verbose_name='重要度', default=0)
    memo = models.CharField(max_length=1000, default='')

   
    class Meta:
       db_table = 'Cust_info'
       
    def __str__(self):
        return  self.Cust_name 