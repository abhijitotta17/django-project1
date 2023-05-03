from django.shortcuts import render
from demo1.models import ModelStudent
from demo1 import forms2
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
    #l=list(ModelStudent.objects.all().values_list().filter(name='Ankita otta'))
    l='Work under progress'  
    return render(request,'signin.html',{'l':l})






