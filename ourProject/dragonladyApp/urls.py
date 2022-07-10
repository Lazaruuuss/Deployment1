from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    path('Homepage', views.home, name='Homepage'),
    path('About', views.about, name='About'),
    path('Login', views.signin, name='Login'),
    path('AdminLogin', views.adminsignin, name='AdminLogin'),
    path('Logout', views.logoutuser, name='Logout'),
    path('Register', views.Register, name='Register'),

    path('Contact_Us', views.contact_us, name='Contact Us'),
    path('FAQs', views.faqs, name='FAQs'),
    path('Sitemap', views.sitemap, name='Sitemap'),
    path('Privacy_Policy', views.privacy_policy, name='Privacy Policy'),
    path('Terms_and_Conditions', views.terms_and_conditions, name='Terms and Conditions'),
    path('Support', views.support, name='Support'),



    #Admin 
    path('3.1_Admin_Home.html', views.admin_home, name='Admin Homepage'),
    path('Admin_Borrower', views.admin_borrower, name='Admin_Borrower'),
    path('Borrower_List', views.pdf_borrowerlist, name='Borrower_List'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('Admin_Loan', views.admin_loan, name='Admin Loan'),
    path('Admin_Payment', views.admin_payment, name='Admin Payment'),

    path('Admin_Contact_Us', views.admin_contact_us, name='Admin Contact Us'),
    path('Admin_FAQs', views.admin_faqs, name='Admin FAQs'),
    path('Admin_Sitemap', views.admin_sitemap, name='Admin Sitemap'),
    path('Admin_Privacy_Policy', views.admin_privacy_policy, name='Admin Privacy Policy'),
    path('Admin_Terms_and_Conditions', views.admin_terms_and_conditions, name='Admin Terms and Conditions'),
    path('Admin_Support', views.admin_support, name='Admin Support'),


 
    #Borrower
    path('Borrower_Home', views.borrower_home, name='Borrower_Home'),
    path('Borrower_Account', views.borrower_account, name='Borrower_Account'),
    path('Borrower_Loan', views.Borrower_Loan, name='Borrower_Loan'),
    path('Borrower_Payment', views.Borrower_Payment, name='Borrower_Payment'),
    path('Borrower_History', views.Borrower_History, name='Borrower_History'),
    path('Borrower_Contact_Us', views.borrower_contact_us, name='Borrower Contact Us'),
    path('Borrower_FAQs', views.borrower_faqs, name='Borrower FAQs'),
    path('Borrower_Sitemap', views.borrower_sitemap, name='Borrower Sitemap'),
    path('Borrower_Privacy_Policy', views.borrower_privacy_policy, name='Borrower Privacy Policy'),
    path('Borrower_Terms_and_Conditions', views.borrower_terms_and_conditions, name='Borrower Terms and Conditions'),
    path('Borrower_Support', views.borrower_support, name='Borrower Support'),
]