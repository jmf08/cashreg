from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.login, name='login'),
   path('Inventory/', views.inventory, name='inventory'),
   path('Inventory/Inventory', views.inventory, name='inventory'),
   path('Inventory/CashRegister', views.Cash_Register, name='CashRegister'),
   path('Inventory/CashRegIframe', views.Cash_Regiframe, name='CashRegIframe'),
   path('Inventory/Add Inventory',views.Add_inventory, name='AddInventory'),
   path('CashRegister/', views.Cash_Register, name='CashRegister'),
   path('CashRegister/CashRegIframe/',views.Cash_Regiframe, name='CashRegIframe'),
   path('CashRegIframe/',views.Cash_Regiframe, name='CashRegIframe'),
   path('Inventory/login', views.login, name='login'),
   path('Signup/',views.signup, name= 'Signup'),
   path('Signup/login',views.login, name= 'login'),
   path('login', views.login, name='login'),
   path('CashRegister/login',views.login, name= 'login'),
   path('CashRegister/Inventory',views.inventory, name= 'Inventory'),
   path('CashRegister/CashRegister', views.Cash_Register, name='CashRegister'),
   path('CashRegister/Add Inventory',views.Add_inventory, name='AddInventory'),
]
