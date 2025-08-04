from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                person = Signup.objects.get(user=user)
                if person.status == "Confirm":
                    auth.login(request,user)
                    error = "not"
                elif person.status == "Pending":
                    error='wait'
                else:
                    error="out"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error,'error':error}
    return render(request,'login.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,image=i,gender=gen,address=addr,dob=d,status="Pending")
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    data = Signup.objects.get(user=request.user)
    d = {'data':data}
    return render(request,'user_home.html',d)

def logout(request):
    auth.logout(request)
    return redirect('/')

def users(request):
    data = Signup.objects.all()
    data = data[::-1]
    d = {'data':data}
    return render(request,'users.html',d)

def delete_user(request,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('users')


def user_status(request,id):
    error=""
    data=User.objects.get(id=id)
    data2=Signup.objects.get(user=data)
    if request.method=='POST':
        s = request.POST['status']
        data2.status = s
        try:
            data2.save()
            error="no"
        except:
            error="yes"
    d={'data':data,'data2':data2,'error':error}
    return render(request,'user_status.html',d)

def complain(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        com = request.POST['complain']
        try:
            Complain.objects.create(name=n,email=e,contact=c,complain=com)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'complain.html',d)

def book_gas(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        gt = request.POST['gas']
        p = request.POST['price']
        dt = request.POST['booking-date']
        gid = request.POST['gid']
        mon = request.POST['month']
        gno = request.POST['gidn']
        a = request.POST['address']
        try:
            Booking.objects.create(name=n,email=e,contact=c,gastype=gt,price=p,month=mon,day=dt,idtype=gid,idno=gno,address=a,status="Pending")
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'book_gas.html',d)

def view_booking(request):
    data = Booking.objects.all();
    data = data[::-1]
    d = {'data':data}
    return render(request,'view_booking.html',d)

def delete_booking(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('view_booking')

def booking_status(request,id):
    error=""
    data = Booking.objects.get(id=id)
    if request.method=='POST':
        s = request.POST['status']
        data.status = s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'booking_status.html',d)

def my_booking(request):
    data = Booking.objects.filter(email=request.user)
    d = {'data':data}
    return render(request,'my_booking.html',d)

def view_complains(request):
    data = Complain.objects.all()
    d = {'data':data}
    return render(request,'view_complains.html',d)

def delete_complain(request,id):
    data = Complain.objects.get(id=id)
    data.delete()
    return redirect('view_complains')

#fot current Date and Time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def pay_now(request,id):
    error=""
    data = Booking.objects.get(id=id)
    if request.method=='POST':
        n = data.name
        e = data.email
        c = data.contact
        p = data.price
        m = "By Card"
        s = "Success"
        pt = dt_string
        gt = data.gastype
        bt = data.day
        data.status = "Paid"
        try:
            Payment.objects.create(name=n,email=e,contact=c,price=p,mode=m,status=s,paymentdate=pt,gastype=gt,day=bt,invoiceid=id)
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'pay_now.html',d)

def invoice(request,id):
    data = Payment.objects.get(invoiceid=id)
    d = {'data':data}
    return render(request,'invoice.html',d)

def edit_profile(request):
    error=""
    data=User.objects.get(id=request.user.id)
    data2=Signup.objects.get(user=request.user)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        g = request.POST['gender']
        do = request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=do
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
        try:
            i=request.FILES['profilepic']
            data2.image=i
            data2.save()
            error="no"
        except:
            pass
    d={'data':data,'data2':data2,'error':error}
    return render(request,'edit_profile.html',d)

def search(request):
    n=request.POST['name']
    data = Booking.objects.filter(name__icontains=n)
    d={'data':data}
    return render(request,'view_booking.html',d)

def searchday(request):
    n=request.POST['name2']
    data = Booking.objects.filter(day__icontains=n)
    d={'data':data}
    return render(request,'view_booking.html',d)

def search2(request):
    n=request.POST['name2']
    data = Booking.objects.filter(day__icontains=n).filter(email=request.user)
    d={'data':data}
    return render(request,'my_booking.html',d)


