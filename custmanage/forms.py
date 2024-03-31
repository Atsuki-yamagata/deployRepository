from django import forms
from .models import CustInfo, Users
from datetime import datetime
from django.shortcuts import get_object_or_404


class CustInfoForm(forms.ModelForm):
    class Meta:
        model = CustInfo
        fields = '__all__'
    def save(self, *args, **kwargs):
        obj = super(CustInfo, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj
    

class CustUpdateForm(forms.ModelForm):

    class Meta:
        model = CustInfo
        fields = ['Cust_name', 'Company', 'Company_address', 'Cust_post', 'Cust_job', 'Cust_skill',
                  'Cust_mail', 'Cust_phone_num', 'importance_level', 'memo']

    def save(self, *args, **kwargs):
        obj = super(CustUpdateForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj
    
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
    def save(self, *args, **kwargs):
        obj = super(Users, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj
    
class UserUpdateForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = ['name', 'age', 'address', 'hobby', 'job', 'job_history',
                  'skill', 'post', 'mail', 'phone_num', 'memo']
        
        
class CustUpdateForm(forms.ModelForm):

    class Meta:
        model = CustInfo
        fields = ['Cust_name', 'Company', 'Company_address', 'Cust_post', 'Cust_job', 
                  'Cust_skill','Cust_mail', 'Cust_phone_num', 'importance_level', 'memo']
