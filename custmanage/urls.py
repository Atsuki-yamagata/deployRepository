from django.urls import path
from .views import (CustomerListView, CustDetailView, CustCreateView,
                    CustDeleteView, UserListView, CustUpdateView,
                    UserUpdateView, UserDeleteView)
from . import views

app_name = 'custmanage'
urlpatterns = [
    path('user_info/<int:pk>/', UserListView.as_view(), name='user_info'),
    path('cust_list/', CustomerListView.as_view(), name='cust_list'),
    path('cust_detail/<int:pk>/', CustDetailView.as_view(), name='cust_detail'),
    path('edit_user_info/<int:pk>/', UserUpdateView.as_view(), name='edit_user_info'),
    path('edit_cust_info/<int:pk>/', CustUpdateView.as_view(), name='edit_cust_info'),
    path('add_cust_info/', CustCreateView.as_view(), name='add_cust_info'),
    path('delete_info/<int:pk>/', CustDeleteView.as_view(), name='delete_info'),
    path('delete_user/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
]