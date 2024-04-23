from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Register
from work.models import User,Taskmodel
from work.forms import Loginform
from django.contrib.auth import authenticate,login,logout
from work.forms import Taskform
from django.contrib import messages
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,**kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
        else:
            return fn(request,**kwargs)
    return wrapper 
# ================================== login cheyyatha aalkk task add cheyyan paadilla athin vendi decroter use cheyth ayale login pageilekk aakitt login cheytha shesham task add akkan anuvadhikugha ====================
# ============================================================ login cheytha userin mathrame delete cheyyan pattollu ayalude datas

def mylogin(fn):
    def wrapper(request,**kwargs):
        id=kwargs.get('pk')
        obj=Taskmodel.objects.get(id=id)
        if obj.user!=request.user:
            return redirect('signin')
        else:
            return fn(request,**kwargs)
    return wrapper


# ====================================================================================
class Registration(View):                      # form - register
    def get(self,request,**kwargs):
        form=Register()
        return render(request,"register.html",{'form':form})
    
    def post(self,request,**kwargs):
        form=Register(request.POST)

        if form.is_valid():
            # form.save()   it is not safe we provide query for safety of data

            User.objects.create_user(**form.cleaned_data)    # serveril nninum password poleulla sathanghal ini vaayikan pattilla athin vendi django secure aaki
            form=Register()
        return redirect('reg')            # username poleolla details okke adichitt nere taskmodel pageilekk direct poyikolum
# =======================================  log in   =========================================

class Sighnin(View):
    def get(self,request,**kwargs):
        form=Loginform()
        return render(request,'login.html',{"form":form})
    
    def post(self,request,**kwargs):

        form=Loginform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)

            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")

            user_obj=authenticate(username=u_name,password=pwd)    # cross check cheyyan venditt aanu authenticate fnctn use cheyunath 
            if user_obj:
                print("valid credentials")

                login(request,user_obj)     # login oru fnctn aanu 
                return redirect("reg")
            else:
                form=Loginform()
                print("invalid")
                return render(request,"login.html")
# ===========================================================================

@method_decorator(signin_required,name='dispatch')
class Add_task(View):
    def get(self,request,**kwargs):

        form=Taskform()
        # data=Taskmodel.objects.all().order_by('completed')   # completed addeel varan not completed adhyam vaaran
        data=Taskmodel.objects.filter(user=request.user).order_by('completed')
        return render(request,"index.html",{"form":form,"data":data})
    def post(self,request,**kwargs):
        form=Taskform(request.POST)

        if form.is_valid():
            form.instance.user=request.user   # form nte details tableil add avunna kuutathil login cheytha user nte details kuude add avanam athin vendit aanu ith foreign kond connect aakittund but fetch cheyyan paatilla....userude id aayirikum task tableil add avanne ath fetch cheytha ella detailsum kittum
            
            #req.user=get the authenticated user(login cheyunna userude name)
            form.save()
            messages.success(request,"Task Added Successfully")   # import cheyyanaam
        form=Taskform()
        # data=Taskmodel.objects.all().order_by('completed')         # tabelilolla data full kaanan venditt annu ath vere class aayitt kodukanda.adiyil vannolum arokke add akitundo avrde okke
        data=Taskmodel.objects.filter(user=request.user).order_by('completed')
        return render(request,"index.html",{"form":form,"data":data})
        
# =============================================== delete ============================

@method_decorator(signin_required,name='dispatch')
@method_decorator(mylogin,name='dispatch')

class Delete_task(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        Taskmodel.objects.get(id=id).delete()
        return redirect("reg")


class Task_edit(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Taskmodel.objects.get(id=id)
        if obj.completed==False:
            obj.completed=True
            obj.save()
        return redirect("reg")

# ============================== logout =====================
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('signin')    #import cheyyanaam

# =====================================   delete user ac =====================

class user_delete(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        data=User.objects.get(id=id).delete()
        return redirect('signin')
# ================================================
