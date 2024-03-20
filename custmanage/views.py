from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import os
from . import forms
from .models import CustInfo, Users
from django.core.exceptions import ValidationError
from django.http import HttpResponse, Http404
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .forms import CustUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied



# Create your views here.

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_user_func(self):
        Users = get_object_or_404(Users, pk=self.kwargs['pk'])
        return self.get_queryset().filter(user_id=self.request.user.id).exists()

    def test_cust_func(self):
        Cust_info = get_object_or_404(CustInfo, pk=self.kwargs['pk'])
        return self.get_queryset().filter(user_id=self.request.user.id).exists()
    
    def test_func(self):
        if self.test_user_func() or self.test_cust_func():
            return True
        else:
            raise PermissionDenied
    
class UserListView(LoginRequiredMixin, ListView, OnlyYouMixin):
    model = Users
    template_name = os.path.join('custmanage', 'user_info.html')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id).order_by('id')

class CustomerListView(LoginRequiredMixin, ListView, OnlyYouMixin):
    model = CustInfo
    template_name = os.path.join('custmanage', 'cust_list.html')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id).order_by('id')

    
    # 絞り込み
    def get_queryset_sort(self):
            query = super().get_queryset()
            Company = self.request.GET.get('Company', None)
            Cust_job = self.request.GET.get('Cust_job', None)
            Cust_skill = self.request.GET.get('Cust_skill', None)
            if Company:
                query = query.filter( Company=Company )
            if Cust_job:
                query = query.filter( Cust_job=Cust_job )
                
            if Cust_skill:
                query = query.filter( Cust_skill=Cust_skill )
                
            order_by_importance_level = self.request.GET.get('order_by_importance_level', 0)
            if order_by_importance_level == '1':
                query = query.order_by('importance_level')
            elif order_by_importance_level == '2':
                query = query.order_by('-importance_level')
            return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Company'] = self.request.GET.get('Company', '')
        context['Cust_job'] = self.request.GET.get('Cust_job', '')
        context['Cust_skill'] = self.request.GET.get('Cust_skill', '')
        order_by_importance_level = self.request.GET.get('order_by_price', 0)
        if order_by_importance_level == '1':
            context['ascending'] = True
        elif order_by_importance_level == '2':
            context['descending'] = True
        return context

class CustCreateView(CreateView, OnlyYouMixin, LoginRequiredMixin):
    model = CustInfo
    fields = ['Cust_name', 'Company', 'Company_address', 'Cust_post', 'Cust_job', 'Cust_skill',
              'Cust_mail', 'Cust_phone_num', 'importance_level', 'memo']
    template_name = os.path.join( 'custmanage', 'add_cust_info.html')
    success_url = reverse_lazy('custmanage:cust_list')


    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        return super(CustCreateView, self).form_valid(form)
        
class CustDetailView(LoginRequiredMixin, DetailView, OnlyYouMixin):
    model = CustInfo
    template_name = os.path.join('custmanage', 'cust_detail.html')
              
class CustDeleteView(LoginRequiredMixin, DeleteView, OnlyYouMixin):
    model  = CustInfo
    template_name = os.path.join('custmanage','delete_info.html')
    success_url = reverse_lazy('custmanage:cust_list')

class UserDeleteView(LoginRequiredMixin, DeleteView, OnlyYouMixin):
    model  = Users
    template_name = os.path.join('custmanage','delete_user.html')
    
    def get_success_url(self):
        return reverse_lazy('accounts:user_login')

    
class CustUpdateView(LoginRequiredMixin, UpdateView, OnlyYouMixin):
    model = CustInfo
    template_name = os.path.join('custmanage', 'update_cust_info.html')
    
class UserUpdateView(UpdateView, OnlyYouMixin):
    model = Users
    form_class = UserUpdateForm
    template_name = 'custmanage/edit_user_info.html'
    
    def get_success_url(self):
        return reverse_lazy('custmanage:user_info', kwargs={'pk': self.object.pk})
    
class CustUpdateView(UpdateView, OnlyYouMixin, LoginRequiredMixin):
    model = CustInfo
    form_class = CustUpdateForm
    template_name = 'custmanage/edit_cust_info.html'
    
    def get_success_url(self):
        return reverse_lazy('custmanage:cust_detail', kwargs={'pk': self.object.pk})
    
