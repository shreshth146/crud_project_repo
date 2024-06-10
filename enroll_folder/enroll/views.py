from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistation
from .models import user
# Create your views here.

def add_show(request):
    if request.method =='POST':
        am= StudentRegistation(request.POST)
        if am.is_valid():
           nm= am.cleaned_data['name']
           em =am.cleaned_data['email']
           pw = am.cleaned_data['password']
           reg=user(name=nm,email=em,password=pw)
           reg.save()
           am= StudentRegistation()
    else:
        am=StudentRegistation()
    stud= user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':am, 'stu':stud} )


# this function will delete items
def delete_data(request, id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        am=StudentRegistation(request.POST, instance=pi)
        if am.is_valid():
            am.save()
    else:
     pi=user.objects.get(pk=id)
     am= StudentRegistation(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':am})
