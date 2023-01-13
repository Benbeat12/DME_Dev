from django.urls import path
from CUA.views import register, registerCustomer, registerDeveloper, userLogin, dashboard, customerDash, developerDash


app_name = 'CUA'

urlpatterns = [
    path('register/', register, name='register'),
    path('registerCustomer/', registerCustomer, name='registerCustomer'),
    path('registerDeveloper/', registerDeveloper, name='registerDeveloper'),
    path('login/', userLogin, name='userLogin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customerDash/', customerDash, name='customerDash'),
    path('developerDash/', developerDash, name='developerDash'),

]

