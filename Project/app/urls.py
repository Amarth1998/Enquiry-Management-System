from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("UserRegistration/", views.UserRegistration, name="UserRegistration"),
    path("uregistration_insert/", views.uregistration_insert, name="uregistration_insert"),
    path("UserLogin/", views.UserLogin, name="UserLogin"),
    path("userloginpage_fetch/", views.userloginpage_fetch, name="userloginpage_fetch"),
      
#==============================================================================================
    path("AdminLogin/", views.AdminLogin, name="AdminLogin"),
    path("AdminRegistration/", views.AdminRegistration, name="AdminRegistration"),
    path("adminDashboard/", views.adminDashboard, name="adminDashboard"),
    path("adminloginpage_fetch/", views.adminloginpage_fetch, name="adminloginpage_fetch"),
    path("aregistration/", views.aregistration, name="aregistration"),
    
#===============================================================================================
     path("GoToEnquiry/", views.GoToEnquiry, name="GoToEnquiry"),
     path('enquiryinsert/',views.enquiryinsert,name='enquiryinsert'),    
     path('EnquiryPageAdmin/',views.EnquiryPageAdmin,name='EnquiryPageAdmin'),
     
     
    path('updateEquiry/<int:pk>/',views.UpdateEquiry,name='UpdateEquiry'),
    path('UpdateData/<int:pk>/',views.UpdateData,name='UpdateData'),
    path('delete/<int:pk>/',views.DeleteData,name='deleteData'),

 
]
