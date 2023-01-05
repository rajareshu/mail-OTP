from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
import random

def home(request):
    return render(request,"index.html")
    
def sendmail(request):
    if request.method=='POST':
        subject = 'otp'
        t=random.random()
        t=t*10000
        t=int(t)
        message = str(t)
        email_from = settings.EMAIL_HOST_USER
        email=request.POST['email']
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'confirm.html',{'otp':t})
    else:
        return render(request,'sendmail.html')

def verify(request):
    otp=request.POST['otp']
    votp=request.POST['votp']
    if otp==votp:
        return render(request,'enterdetails.html')
    else:
        return render(request,'sendmail.html')

