from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

#Registration (Create Account)
class Registration (AbstractUser):
    gender = [
        ('M','Male'),
        ('F','Female'),
        ('NB','Non-Binary'),
        ('T','Transgender'),
        ('I','Intersex'),
        ('IPNTS','I prefer not to say'),
    ]

    username = models.EmailField (unique=True)
    middle_name = models.CharField (max_length=50, blank=True, verbose_name="middle_name")
    age = models.IntegerField (blank=True, verbose_name="age")
    birthday = models.DateField (blank=True, verbose_name="birthday")
    gender = models.CharField (max_length=50, choices=gender, default="Male", verbose_name="gender")
    home_address = models.CharField (max_length=50, blank=True, verbose_name="home_address")

    class Meta:
        db_table = "dragonladyApp_Registration"

#Borrower (Loan-making) 
class ApplyLoan (Model): 
    mode_of_loan_transfer = [
        ('GC','Gcash'),
        ('PM','Paymaya'),
        ('PP','Paypal'),
        ('BDO','BDO'),
        ('WI','Walk-In'),
        ]

    email_address = models.OneToOneField (Registration, on_delete=models.CASCADE)
    to_be_paid = models.IntegerField (blank=False, verbose_name="to_be_paid")
    loan_date = models.DateField (blank=False, verbose_name="loan_date")
    amount_of_loan = models.IntegerField (blank=False, verbose_name="amount_of_loan")
    mode_of_loan_transfer = models.CharField (max_length=50, blank=False, choices=mode_of_loan_transfer, default="Gcash", verbose_name="mode_of_loan_transfer")
   
    class Meta:
        db_table = "dragonladyApp_ApplyLoan"

#Borrower (Payment-making)
class ApplyPayment (Model):
    mode_of_payment = [
                ('GC','Gcash'),
                ('PM','Paymaya'),
                ('PP','Paypal'),
                ('BDO','BDO'),
                ('WI','Walk-In'),
            ]
            
    email_address = models.OneToOneField (ApplyLoan, on_delete=models.CASCADE)
    payment_date = models.DateField (blank=False, verbose_name="payment_date")
    remaining_balance = models.IntegerField (blank=False, verbose_name="remaining_balance")
    amount_paid = models.IntegerField (blank=False, verbose_name="amount_paid")
    mode_of_payment = models.CharField (max_length=50, blank=True, choices=mode_of_payment, default="Gcash", verbose_name="mode_of_payment")

    class Meta:
        db_table = "dragonladyApp_ApplyPayment"