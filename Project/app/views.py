from django.shortcuts import render,redirect
from .models import AdminDataBase ,UserDataBase ,EnquiryDataBase
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def UserLogin(request):
    return render(request,'app/UserLogin.html')

def UserRegistration(request):
    return render(request,'app/UserRegistration.html')


#====================USER Registration  start=======================================================
def uregistration_insert(request):
     if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        image=request.FILES['image']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = UserDataBase.objects.filter(Email=email)
        if user:
            msg= "User already exist"
            return render(request,'app/UserRegistration.html',{'msg':msg})
        else:
            if password==cpassword:
                newdatainsert = UserDataBase.objects.create(FirstName=fname,lastName=lname,Email=email,Image=image,Contact=contact,Password=password)
                msg = "User register Successfully"
                return render(request,'app/UserRegistration.html',{'msg':msg})
            else:
                msg="Password and Confirm Password not match!"
                return render(request, 'app/UserRegistration.html',{'msg':msg})
     return render(request,'app/UserRegistration.html')


#====================USER Registration end =======================================================
#====================USER Login start =======================================================
def userloginpage_fetch(request):
    if request.method=='POST':
        # print(request.POST)
        a=request.POST['email']
        p=request.POST['password']
        user=UserDataBase.objects.get(Email=a)
        if user:
            if user.Password==p:
                mydata = UserDataBase.objects.filter(Email=a).values()
                print(mydata)
                return render(request,'app/userDashboard.html',{'msg':mydata})
        else:
            msg="First Name not matched"
            return render(request,'app/UserLogin.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'UserRegistration.html',{'msg':msg})


#====================USER Login end =======================================================






#=============================ADMIN=======================================
def AdminLogin(request):
    return render(request,"app/AdminLogin.html")
def AdminRegistration(request):
    return render(request,"app/AdminRegistration.html")

#=====================admin login===========================================================================
def adminloginpage_fetch(request):
    if request.method=='POST':
        # print(request.POST)
       
        a=request.POST['email']
        p=request.POST['password']
        user=AdminDataBase.objects.get(Email=a)
        # print(user.values())
        # print(user.fname)
        if user:
            if user.Password==p:
                mydata = AdminDataBase.objects.filter(Email=a).values()
                print(mydata)
                return render(request,'app/adminDashboard.html',{'msg':mydata})
        else:
            msg="First Name not matched"
            return render(request,'app/AdminLogin.html',{'msg':msg})
    else:
        msg="user dose not exit please register first"
        return render(request,'app/AdminLogin.html',{'msg':msg})
#=====================admin login end================================================ 
#=======================ADMIN REGISTRATION================================================================
def aregistration(request):
     if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        image=request.FILES['image']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = AdminDataBase.objects.filter(Email=email)
        if user:
            msg= "User already exist please login"
            return render(request,'app/AdminRegistration.html',{'msg':msg})
        else:
            if password==cpassword:
                newdatainsert = AdminDataBase.objects.create(FirstName=fname,lastName=lname,Email=email,Image=image,Contact=contact,Password=password)
                msg = "User register Successfully go to admin login page"
                return render(request,'app/AdminRegistration.html',{'msg':msg})
            else:
                msg="Password and Confirm Password not match!"
                return render(request, 'app/AdminRegistration.html',{'msg':msg})
     return render(request,'app/AdminRegistration.html')
 #=======================ADMIN REGISTRATION end=====================================================================

def adminDashboard(request):
     return render(request,'app/adminDashboard.html')
 
 
 
 
 
#=============================================================================================
def GoToEnquiry(request):
    return render(request,'app/userEnquiry.html')

def enquiryinsert(request):
    if request.method=='POST':
        studentname=request.POST["studentname"]
        contact=request.POST["contact"]
        email=request.POST["email"]
        enquiry=request.POST["enquiry"]
        user = EnquiryDataBase.objects.create(Studentname=studentname,Contact=contact,Email=email,Enquiry=enquiry)
        msg= "Enquiry Successfully"
        return render(request,'app/userEnquiry.html',{"msg":msg})
#=====================================================================================

def EnquiryPageAdmin(request):
    alldata=EnquiryDataBase.objects.all()
    return render(request,'app/EnquiryPageAdmin.html',{'k':alldata})

#===================================#fetching the data of perticular ID========
def UpdateEquiry(request,pk):
    
    getdata=EnquiryDataBase.objects.get(id=pk)
    return render(request,'app/UpdateEquiry.html',{'k1':getdata})

#==================================Update====================================================== data View
def UpdateData(request,pk):
    udata=EnquiryDataBase.objects.get(id=pk)
    udata.Studentname=request.POST['studentname']
    udata.Enquiry=request.POST['enquiry']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    #Query for update
    udata.save()
    return redirect('EnquiryPageAdmin')

#=====================================Delete======================================================== data View
def DeleteData(request,pk):
    ddata=EnquiryDataBase.objects.get(id=pk)
    #Query for delete
    ddata.delete()
    return redirect('EnquiryPageAdmin')



#