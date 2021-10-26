from django.shortcuts import render 
#from django.http import HttpResponse

def login(request):
   #return HttpResponse("Welcome to website")
   return render(request, 'acts/Log-in 1.html')
def inventory(request):
   return render(request, 'acts/Inventory 4.html')
def Add_inventory(request):
   return render(request, 'acts/Add Inventory 5.html')
def Cash_Register(request):
   return render(request, 'acts/Cash Register 3.html')
def Cash_Regiframe(request):
   return render(request, 'acts/CashRegIframe.html')
def signup (request):
   return render(request, 'acts/Create New Account 2.html')