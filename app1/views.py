from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login
import uuid
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .q_form import UpadteUser

# Create your views here.

#function for login and after sucessfull login redirect to home page
def login_page(request):
    if request.method == 'POST':
        form = request.POST
        u = form.get('name')
        ps = form.get('password')
        user_ob = CustomUser.objects.filter(username=u).first()

        if user_ob is None:
            messages.success(request,'Invalid User.. !!')
            return redirect('/')
        if not user_ob.is_verify:
            messages.success(request,'Verify email,check mail ')
            return redirect('/')
        #user = authenticate(username=u,password=ps)
        user = authenticate(username=u, password=ps)

        if user is None:
            messages.success(request,'Invalid creditinal.. !!')
            return redirect('/')
        else:
            o = CustomUser.objects.filter(username=u)
            login(request,user)
            return redirect('/home')
            return render(request,'home.html',{'o':o})

    return render(request,'login.html')

#function for register user
def register(request):
    if request.method == 'POST':
        form = request.POST
        u = form.get('username')
        e = form.get('email')
        ps = form.get('password')
        f = form.get('fname')
        l = form.get('lname')
        auth_token = str(uuid.uuid4())
        user_ob = CustomUser(username=u,email=e,auth_token=auth_token,first_name=f,last_name=l)
        user_ob.set_password(ps)
        user_ob.save()
        send_mail_to_verify(e,auth_token)
        return redirect('/token')

    return render(request,'register.html')

#function to undestand the user that verification link send
def token(request):
    return render(request,'token.html')

def home(request):
    usr = request.user
    o = CustomUser.objects.filter(username=usr)
    na = request.user
    return render(request,'home.html',{'o':o,'na':na})

# function for send mail to user given mail id to verify email
def send_mail_to_verify(email,token):
    subject = 'verify link'
    message = f'hi verify link http://127.0.0.1:8000/verify/{token}'
    email_form =settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)

#function for verification of email if verify email then susefully login and redirct to home else redirct to login with eror message
def verify_mail(request,auth_token):
    try:
        user_ob = CustomUser.objects.filter(auth_token=auth_token).first()

        if user_ob:
            user_ob.is_verify=True
            user_ob.save()
            return redirect('/')
    except Exception:
        return redirect('/')

#function for forget password or change password
def forget(request):
    if request.method == 'POST':
        form = request.POST
        p1 = form.get('password')
        p2 = form.get('password2')
        e = form.get('email')
        if p1!=p2:
            messages.success(request,'Password Not Match.... validate......!!')
            return redirect('/forget')
        user_o = CustomUser.objects.filter(email=e).first()
        user_o.set_password(p1)
        return redirect('/')
    return render(request,'forget.html')


a=0
# to calculate bmi of user
def bmi(request):
    global eml
    usr = request.user
    uer_ob=CustomUser.objects.filter(username=usr)
    for i in uer_ob:
        eml = i.email

    if request.method == 'POST':
        f_data = request.POST
        h = f_data.get('height')
        w = f_data.get('weight')
        ih = float(h)/100
        print(ih)
        wi = float(w)
        print(wi)
        h1 = ih**2
        print(h1)
        result =round(wi/h1,2)

        if result < 18.5:
            ob='Underweight'

        elif result>=18.5 or result<25:
            ob=' Normal weight'
        elif result>=25 or result<29.9:
            ob='Overweight'
        elif result >=29.9 or result<35:
            ob='Obese'
        else:
            ob='Morbid obesity'
        bmi_mail(eml,result)


        return render(request,'bmi.html',{'result':result,'ob':ob})

#tempalte for send mail after calculate bmi
def bmi_mail(email,result):
    subject = 'BMI ststus'
    message = f'hi your BMI Sscore is {result} .'
    email_form =settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)

def edit(request,id):
    msg=''
    if request.method == 'POST':
        user_ob = CustomUser.objects.get(id=id)
        form = UpadteUser(request.POST,instance=user_ob)
        if form.is_valid():

            msg = 'User details update sucessfully .. !'
            o=CustomUser.objects.filter(id=id).first()
            form.save()
            return redirect('/home')
    else:
        pi = CustomUser.objects.get(id=id)
        form = UpadteUser(instance=pi)
    return render(request,'update.html',{'form':form})


def delete(request,id):
    if request.method == 'POST':
        pi = CustomUser.objects.get(id=id)
        pi.delete()
        return redirect('/home')
    ob = request.user
    return render(request,'delete.html',{'ob':ob})
