from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from myproject9 import settings
from django.contrib.auth.decorators import login_required
import random
otp=random.randint(1111,9999)
# Create your views here.


def index(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            user=infoform(request.POST)
            if user.is_valid():
                username=user.cleaned_data.get('username')
                try:
                    info.objects.get(username=username)
                    print("Username is already exists!")
                    msg="Username is already exists!"
                except info.DoesNotExist:
                    user.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"
            else:
                print(user.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']
            user=info.objects.filter(username=unm, password=pas)
            fnm=info.objects.get(username=unm)
            uid=info.objects.get(username=unm)

            if user:
                print("login sucess")
                #request.session['user']=unm
                request.session['user']=fnm.firstname
                request.session['uid']=uid.id
            else:
                print("error")
            
    return render(request,'index.html',{'user':user,'msg':msg})









def about(request):
    return render(request,'about.html')


def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        user=feedbackform(request.POST)
        if user.is_valid():
            user.save()
            print("feedback saved ")
            # email

            sub=f"thank you!!"
            msg=f"Dear {request.POST['name']}!\n\nThanks for your feedback, we will connect shortly!\n\nIf any queries regarding, you can contact us\n\n Your one time password is{otp}\n\n+91 9054264505 | help@tops-int.com\n\nThanks & Regards!\nTOPS Tech - Rajkot\nwww.tops-int.com"
            fm_email=settings.EMAIL_HOST_USER
            to_emil=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fm_email,recipient_list=to_emil)
            print("send email")
            return redirect('conform')

        else:
            print(user.errors)
    return render(request,'contact.html',{'user':user})


def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=info.objects.get(id=uid)
    if request.method=='POST':
        user=infoform(request.POST,instance=cuser)
        if user.is_valid():
            user.save()
            print("profile")
        else:
            print(user.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

@login_required
def note(request):
    user=request.session.get('user')
    if request.method=='POST':
        user=noteform(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            print("sent note ")
        else:
            print("error")

    return render(request,'note.html',{'user':user})


def userlogout(request):
    logout(request)
    return redirect('/')



def conform(request):
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("same ")
            return redirect('note')
    return render(request,'conform.html')