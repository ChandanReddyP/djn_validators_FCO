from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
from app.models import *

def create_student(request):
    ESTFO=StudentForm()
    d={'ESTFO':ESTFO}
    if request.method=='POST':
        STFDO=StudentForm(request.POST)
        if STFDO.is_valid():
            sid=STFDO.cleaned_data['sid']
            sn=STFDO.cleaned_data['sn']
            sa=STFDO.cleaned_data['sa']
            em=STFDO.cleaned_data['em']

            SO=Student.objects.get_or_create(sid=sid,sname=sn,sage=sa,semail=em)[0]
            SO.save()
            return HttpResponse('Data created successfully')
        else:
            return HttpResponse('Invalid data')

    return render(request,'create_student.html',d)