from django.shortcuts import render
from demo1.models import ModelStudent
from demo1 import forms2,forms1
from django.http import HttpResponse
# Create your views here.

def stud(request):
    form=forms2.studentFeom()
    if request.method=='POST':
        form=forms2.studentFeom(request.POST)
        if form.is_valid():
            form.save()
            form=forms2.studentFeom()
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
                if  p==l[0][1][-4::]+l[0][-1]:
                    return render(request,'r.html',{'l':list(ModelStudent.objects.all().values().filter(name=g))})
                return HttpResponse('<h1>Invalid password</h1>')
            return HttpResponse('<h1>Invalid user name</h1>')
        
    return render(request,'signin.html',{'form':form})








