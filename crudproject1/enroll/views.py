from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.


# Thsis Function Will Add new iteams and Show all the items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()  # for show blank page
            #fm.save()  ------ Second Save More simple way but we can't acccess the particular data it fetch all the data from the object
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm , 'stu':stud})


 # This function will delete the student from the Database

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# This function will Updata the data

def update_data(request,id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

    return render(request,'enroll/updatestudent.html',{'id':id})