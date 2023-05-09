from django.shortcuts import render,redirect
from demo1.models import ModelStudent
from demo1 import forms2,forms1
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
#from django.contrib.auth.models import User

# Create your views here.

def stud(request):
    form=forms2.studentFeom()
    if request.method=='POST':
        form=forms2.studentFeom(request.POST)
        if form.is_valid():
            form.save()
            form=forms2.studentFeom()
            subject = 'welcome to Softs world'
            message = 'Hi, thank you for registering in softs.\n Your pasword is in the form:\n last 4 characters of your name+regid+phone_num'
            email_from = settings.EMAIL_HOST_USER
            recipient_list =[request.POST['email'],]
            send_mail( subject, message, email_from, recipient_list )

    return render(request,'demo2.html',{'form':form})
def home(request):
    a='HOW ARE YOU. For further information please Register'
    return render(request,'home.html',{'a':a})

def sign(request):
   
    form=forms1.NameForm()
    if request.method=='POST':
        form=forms1.NameForm(request.POST)
        if form.is_valid():
            g=request.POST.get('Username')
            p=request.POST.get('password')
            l=list(ModelStudent.objects.all().values_list().filter(name=g))
            
            if l:
                #for i in l:
                    #if g in i:
                if  p==l[0][1][-4::]+l[0][0]+l[0][-1]:
                    return render(request,'r.html',{'l':list(ModelStudent.objects.all().values().filter(name=g))})
                else:
                    messages.success(request, 'Invalid Password!')
                    return redirect('/signin/')
            else:    #return HttpResponse('<h1>Invalid password</h1>')
                messages.success(request, 'Invalid Username!')
                return redirect('/signin/')
        
    return render(request,'signin.html',{'form':form})








