from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from .form import cr, cr2, cr3, cr4, cr5,CreateUser
from .models import cashreg1, cashreg2, cashreg3
from django.contrib import messages




def Login(request):
   if request.user.is_authenticated:
      return redirect('CashRegister')
   else:
      form = CreateUser()
      if request.method == 'POST':
         form = CreateUser(request.POST)
         username = request.POST.get('username')
         print(username)
         password = request.POST.get('password')
         print(password)
      
         user = authenticate(request, username=username, password=password )
         if user is not None and user.is_superuser:
                login(request, user)
                return redirect('CashRegister')
            
         elif user is not None and user.is_staff:
                login(request, user)
                return redirect('CashRegister')
                
         else:
            messages.info(request, 'Username OR password is incorrect')
      context = {'form':form}
      return render(request, 'acts/Log-in 1.html', context)

@login_required(login_url='Login')
def inventory(request):
   datas = cashreg1.objects.all()
   context = {'datas': datas} 
   print(datas)

   return render(request,'acts/Inventory 4.html', context)

@login_required(login_url='Login')  
def Add_inventory(request):
      form1 = cr()
      if request.method == 'POST':
         form1 = cr(request.POST)
         if form1.is_valid():
            form1.save()
            print(form1)
      context1 = {'form1': form1}
      print(context1)
      return render(request, 'acts/Add Inventory 5.html',context1)


def updateitems(request, update_id):
   data = cashreg1.objects.get(id=update_id)
   form1 = cr(request.POST or None ,instance= data) 
   if form1.is_valid():
      form1.save()
   contexts = {'form1': form1, 'data': data} 
   print(contexts)
   return render(request,'acts/update.html',contexts)

def deleteitems(request, update_id):
   data = cashreg1.objects.get(id=update_id)
   if request.method == "POST":
      data.delete()
      return redirect('inventory')
   context = {'ItemName':data}
   return render(request, 'acts/delete.html', context)

def deleteitems2(request, update_id2):
   data2 = cashreg2.objects.get(id=update_id2)
   if request.method == "POST":
      data2.delete()
      return redirect('CashRegIframe')
   context = {'ItemName2':data2}
   return render(request, 'acts/delete2.html', context)

def deleteitems3(request, update_id3):
   data3 = cashreg3.objects.get(id=update_id3)
   if request.method == "POST":
      data3.delete()
      return redirect('CashRegIframe')
   context = {'Cash3':data3}
   return render(request, 'acts/delete3.html', context)

@login_required(login_url='Login')
def Cash_Register(request):
      formss = cr2()
      formss1 = cr3()
      formss2 = cr4()
      formss3 = cr5()
      if request.method == 'POST':
         formss = cr2(request.POST)
         formss1 = cr3(request.POST)
         formss2 = cr4(request.POST)
         formss3 = cr5(request.POST)
         if formss.is_valid():
            formss.save()
         if formss1.is_valid():
            formss1.save()
         if formss2.is_valid():
            formss2.save()
         if formss3.is_valid():
            formss3.save()
      context = {'formss':formss}
      context1 = {'formss1':formss1}
      print(context)
      print(context1)
      return render(request,'acts/Cash Register 3.html',context)


def Cash_Regiframe(request):
   datas2 = cashreg2.objects.all()
   datas3 = cashreg3.objects.all()
   context = {"datas2": datas2, "datas3": datas3}
   return render(request, 'acts/CashRegIframe.html', context)


def signup (request):
   if request.user.is_authenticated:
        return redirect('CashRegister')
   else:
      form = CreateUser()
      if request.method == 'POST':
         form = CreateUser(request.POST)
         if form.is_valid():
            form.instance.is_staff = True
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('Login')
      print(form)
      context1 = {'form': form}
      print(context1)
      return render(request, 'acts/Create New Account 2.html',context1) 

def logoutUser(request):
   logout(request)
   return redirect('Login')
