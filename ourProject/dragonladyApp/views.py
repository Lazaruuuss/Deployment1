from statistics import mode
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *

from django.http import FileResponse
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate


################Homepage################

def index(request):
    return render (request, 'activities/1_Homepage.html')

def home(request):
    return render (request, 'activities/1_Homepage.html')

def about(request):
    return render (request, 'activities/2_About.html')

def signin(request):
    form = BorrowerLoginForm(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
        
            print (username, password)

            if user is not None and user.is_staff:
                login(request, user)
                return redirect ('Login') 
            elif user is not None:
                login(request, user)
                return redirect ('Borrower_Home')
    return render (request, 'activities/3_Login.html', {'form': form})

def adminsignin(request):
    form = AdminLoginForm(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
        
            print (username, password)

            if user is not None and user.is_staff:
                login(request, user)
                return redirect ('3.1_Admin_Home.html') 
    return render (request, 'activities/3_Login.html', {'form': form})

def Register(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Homepage')
        else:
            print(form)
            print("error")
    context = {'form':form}
    return render (request,'activities/4_Register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('Login')

def contact_us(request):
    return render (request, 'activities/Footer_Contact_Us.html')

def faqs(request):
    return render (request, 'activities/Footer_FAQs.html')

def sitemap(request):
    return render (request, 'activities/Footer_Sitemap.html')

def privacy_policy(request):
    return render (request, 'activities/Footer_Privacy_Policy.html')

def terms_and_conditions(request):
    return render (request, 'activities/Footer_Terms_and_Conditions.html')

def support(request):
    return render (request, 'activities/Footer_Support.html')

################Admin################

@login_required(login_url='Login')
def admin_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Admin_Home.html')
    else:
        return redirect ('Login')
        
@login_required(login_url='Login')
def admin_borrower(request):    
    if request.user.is_authenticated and request.user.is_staff:
        registrations = Registration.objects.filter(is_staff='0')
        return render (request, 'activities/3.1_Admin_Borrower.html', {'registrations':registrations})
    else:
        return redirect ('Login')

def pdf_borrowerlist(request):
    #create byteststream buffer
    buf = io.BytesIO()
    #create document template
    pdf = SimpleDocTemplate(buf, pagesize=letter)
    #content
    registrations = Registration.objects.filter(is_staff='0')
    data = [['First name','Middle name','Last name', 'Username', 'Age','Birthday','Home address']]
    for borrower in registrations:
        data.append([borrower.first_name,borrower.middle_name,borrower.last_name,borrower.username,borrower.age,borrower.birthday, borrower.home_address])
    list = []
    #table
    list.append(Table(data))
    pdf.build(list)
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='Admin_Borrower_List.pdf')

@login_required(login_url='Login')
def admin_loan(request):
    if request.user.is_authenticated and request.user.is_staff:
        registrations = ApplyLoan.objects.all()
        return render (request, 'activities/3.1_Admin_Loan.html', {'registrations':registrations})
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_payment(request):
    if request.user.is_authenticated and request.user.is_staff:
        registrations = ApplyPayment.objects.all()
        return render (request, 'activities/3.1_Admin_Payment.html', {'registrations':registrations})
    else:
        return redirect ('Login')

@login_required(login_url='Login')        
def admin_contact_us(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_Contact_Us.html')
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_faqs(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_FAQs.html')
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_sitemap(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_Sitemap.html')
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_privacy_policy(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_Privacy_Policy.html')
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_terms_and_conditions(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_Terms_and_Conditions.html')
    else:
        return redirect ('Login')

@login_required(login_url='Login')
def admin_support(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render (request, 'activities/3.1_Footer_Support.html')
    else:
        return redirect ('Login')


################Update################

@login_required(login_url='Login')
def edit(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        updateborrower = Registration.objects.get(id=id)
        form = EditBorrower(instance=updateborrower)

        if request.method == 'POST':
            form = EditBorrower(request.POST, instance=updateborrower)
            if form.is_valid():
                form.save()
                return redirect('Admin_Borrower')

        context = {'dragonladyApp' : form}
        return render(request, 'activities/3.1_Admin_Borrower_Update.html', context)
    else: 
        return redirect('Login')
        
################delete################

@login_required(login_url='Login')
def delete(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        deleteborrower = Registration.objects.get(id=id)
        if request.method == 'POST':
            deleteborrower.delete()
            return redirect('Admin_Borrower')

        context = {'dragonladyApp' : deleteborrower}
        return render(request, 'activities/3.1_Admin_Borrower_Delete_Confirmation.html', context)
    else: 
        return redirect('Login')

@login_required(login_url='Login')
def delete1(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        registration = ApplyLoan.objects.get(id=id)
        registration.delete()
        return  HttpResponseRedirect('activities/3.1_Admin_Loan.html')
    else: 
        return redirect('Login')
    
@login_required(login_url='Login')
def delete2(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        registration = ApplyPayment.objects.get(id=id)
        registration.delete()
        return  HttpResponseRedirect('activities/3.1_Admin_Payment.html')
    else: 
        return redirect('Login')
    
################Borrower################

@login_required(login_url='Login')
def borrower_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Borrower_Home.html')

@login_required(login_url='Login')
def borrower_account(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Borrower_Account.html')

@login_required(login_url='Login')
def Borrower_Loan(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        form = BorrowerLoan()
        if request.method == 'POST':
            form = BorrowerLoan(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('Borrower_Home')
            else:
                print(form.errors)
                print("error")
        context = {'form':form}
        return render (request, 'activities/3.2_Borrower_Loan.html', context)

@login_required(login_url='Login')
def Borrower_Payment(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        form = BorrowerPayment()
        if request.method == 'POST':
            form = BorrowerPayment(request.POST)
            if form.is_valid():
                email_address = form.cleaned_data.get("username")
                payment_date = form.cleaned_data.get("payment_date")
                remaining_balance = form.cleaned_data.get("remaining_balance")
                amount_paid = form.cleaned_data.get("amount_paid")
                mode_of_payment = form.cleaned_data.get("mode_of_payment")
                
                ApplyPayment.objects.create(email_address=email_address, payment_date=payment_date, remaining_balance=remaining_balance, amount_paid=amount_paid, mode_of_payment=mode_of_payment)
                form.save()
                return redirect ('Borrower_Home')
        context = {'form': form}
        return render (request, 'activities/3.2_Borrower_Payment.html', context)

def Borrower_History(request) :
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        history = ApplyLoan.objects.all()
        history1 = ApplyPayment.objects.all()
        return render (request, 'activities/3.2_Borrower_History.html',{'history':history,'history1':history1})


def borrower_contact_us(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_Contact_Us.html')

def borrower_faqs(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_FAQs.html')

def borrower_sitemap(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_Sitemap.html')

def borrower_privacy_policy(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_Privacy_Policy.html')

def borrower_terms_and_conditions(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_Terms_and_Conditions.html')

def borrower_support(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('Login')
    else:
        return render (request, 'activities/3.2_Footer_Support.html')