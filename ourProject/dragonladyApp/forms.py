from dataclasses import fields
from logging.config import valid_ident
from socket import fromshare
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.mail import send_mail




class UserRegistration(UserCreationForm):
    gender = [
            ('M','Male'),
            ('F','Female'),
            ('NB','Non-Binary'),
            ('T','Transgender'),
            ('I','Intersex'),
            ('IPNTS','I prefer not to say'),
        ]

    username = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "placeholder": "Enter your Email Address"
            }
        )
    )
   
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "Enter Password"
            }
        )
    )
    
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "placeholder": "Confirm Password"
            }
        )
    )

    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your First Name"
            }
        )
    )

    middle_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Middle Name"
            }
        )
    )

    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Last Name"
            }
        )
    )

    age = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "placeholder": "Enter your Age",
                "maxlength": "2"
            }
        )
    )

    birthday = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Enter your Birthday"
            }
        )
    )

    gender = forms.CharField(
        widget = forms.Select(
            choices = gender,
            attrs={
                "class": "form-control"
            }
        )
    )

    home_address = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Home Address"
            }
        )
    )

    class Meta:
        model = Registration
        fields = ('username', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'age', 'birthday', 'gender', 'home_address')
    
    def save(self):

        user = super().save(commit=False)
        user.email = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.middle_name = self.cleaned_data.get('middle_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.cleaned_data.get('age')
        user.birthday =  self.cleaned_data.get('birthday')
        user.gender = self.cleaned_data.get('gender')
        user.home_address =  self.cleaned_data.get('home_address')
        user.save()

        send_mail('Registration Successful',
            f"""Congratulations! you are now registered. You can sign-in this account to our borrower tab. Please double check your registration.\n
        Here's your username: {user.username}
        Name: {user.first_name} {user.middle_name} {user.last_name}
        Birthday: {user.birthday}
        Address: {user.home_address}
        Age: {user.age}""",

            'dragonladyloaningsystem@gmail.com',
            [f'{user.email}'],
            fail_silently=False)

        return user

class EditBorrower(ModelForm):
    gender = [
            ('M','Male'),
            ('F','Female'),
            ('NB','Non-Binary'),
            ('T','Transgender'),
            ('I','Intersex'),
            ('IPNTS','I prefer not to say'),
        ]

    username = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "placeholder": "Enter your Email Address"
            }
        )
    )
   
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your First Name"
            }
        )
    )

    middle_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Middle Name"
            }
        )
    )

    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Last Name"
            }
        )
    )

    age = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "placeholder": "Enter your Age",
                "maxlength": "2"
            }
        )
    )

    birthday = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Enter your Birthday"
            }
        )
    )

    gender = forms.CharField(
        widget = forms.Select(
            choices = gender,
            attrs={
                "class": "form-control"
            }
        )
    )

    home_address = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter your Home Address"
            }
        )
    )

    class Meta:
        model = Registration
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'age', 'birthday', 'gender', 'home_address')

class BorrowerLoginForm (forms.Form):
    username = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your Email Address"
            }
        )
    )
   
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"
            }
        )
    )

    class Meta:
        model = Registration
        fields = ('username', 'password')

class AdminLoginForm (forms.Form):
    username = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your Email Address"
            }
        )
    )
   
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"
            }
        )
    )

    class Meta:
        model = Registration
        fields = ('username', 'password')


class BorrowerLoan(ModelForm):

    loan_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Enter Date Today"
            }
        )
    )

    amount_of_loan = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "placeholder": "Enter Amount of Loan"
            }
        )
    )

    mode_of_loan_transfer = [
        ('GC','Gcash'),
        ('PM','Paymaya'),
        ('PP','Paypal'),
        ('BDO','BDO'),
        ('WI','Walk-In'),
        ]
    
    mode_of_loan_transfer = forms.CharField(
        widget = forms.Select(
            choices = mode_of_loan_transfer,
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = ApplyLoan
        fields = ('email_address', 'loan_date', 'amount_of_loan', 'mode_of_loan_transfer')
    
class BorrowerPayment(ModelForm):

    payment_date = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Enter Date Today"
            }
        )
    )

    class Meta:
        model = ApplyPayment
        fields = ('email_address', 'payment_date', 'remaining_balance', 'amount_paid', 'mode_of_payment')