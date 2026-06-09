from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



def registerPage(req):
    if req.method == 'POST':
       form = CustomUserCreationForm(req.POST)
       if form.is_valid():
            form.save()
            messages.success(req, "Registration successful! Please log in.")
            return redirect('loginPage')
    
    form = CustomUserCreationForm(req.POST)
    context = {
        'form':form,
        'title':'Register Form',
        'btn':'Register'
    }


    return render(req, 'account/baseAuth.html',context)

       
def loginPage(req):
    if req.method == 'POST':
       form = AuthForm(req,req.POST)
       if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req, "Login successful!")
            return redirect('dashboardpage')
    
    form = AuthForm(req.POST)
    context = {
        'form':form,
        'title':'login Form',
        'btn':'Login'
    }

    return render(req, 'account/baseAuth.html',context)
        
               
          
def logoutPage(req):
    logout(req)
    return redirect('loginPage')

@login_required
def profilePage(req):
    try:
        user = req.user.profile
    except ProfileModel.DoesNotExist:
        user = ProfileModel(user=req.user)
    if req.method == 'POST':
        form = ProfileForm(req.POST, req.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(req, "Profile updated successfully!")
            return redirect('home')



    form = ProfileForm(instance=user)
    context = {
        'form': form,
        'title':'Update Profile Form',
        'btn':'Update'
    }
    return render(req, 'base/baseForm.html', context)



def addCashPage(req):

    if req.method == 'POST':
        form = AddCashForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user = req.user
            user.save()
            messages.success(req, "Cash added successfully!")
            return redirect('dashboardpage')
        

    add = AddcashModel.objects.filter(user=req.user)
    form = AddCashForm()
    context={
        'form': form,
        'Add':add,
        'title':'Add Cash',
        'btn':'Add'
    }

    return render(req, 'baseForm.html', context)

def expendCashPage(req):

    if req.method == 'POST':
        form = ExpendForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user = req.user
            user.save()
            messages.success(req, "Expense recorded successfully!")
            return redirect('dashboardpage')
        

    expend = ExpaendModel.objects.filter(user=req.user)
    form = ExpendForm()
    context={
        'form': form,
        'expend':expend,
        'title':'Expend Cash',
        'btn':'Expend'
    }

    return render(req, 'baseForm.html', context)

def dashboardpage(req):
    data = ProfileModel.objects.filter(user=req.user)

    add_cash = AddcashModel.objects.filter(user = req.user)
    exp = ExpaendModel.objects.filter(user = req.user)

    total_income = add_cash.aggregate(total = Sum('amount'))['total'] or 0
    total_expense = exp.aggregate(total = Sum('amount'))['total'] or 0

    total_save = total_income - total_expense


    context = {
        'data': data,
        'add_cash': add_cash,
        'exp': exp,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_save': total_save,
     
    }
    return render(req, 'dashboard.html', context)
