from django.contrib import messages
from django.db.models.query_utils import refs_expression
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

# This Function Will Add and Show Items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            messages.success(request,'Data insert successful')
        
    else:
        
        fm = StudentRegistration()
        #messages.error(request,'Data not insert') #, extra_tags='alert'
    stud = User.objects.all()
    return render(request,'home.html', {'form':fm,'stu':stud})

# This Function Will Update/Edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
        messages.warning(request,'Data update successful !')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render (request, 'update.html',{'form':fm})

# This Function Will Delete Student
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.error(request,'User delete successful !')
        return HttpResponseRedirect('/')
