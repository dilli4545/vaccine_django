from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Destination

# Create your views here.


def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        aadhar = request.POST['aadhar']
        location = request.POST['addresss']
        zone = request.POST['zone']
        vaccine = request.POST['vaccine']
        dose = request.POST['dose']
        time = request.POST['time']

        a= Destination(name=name,age=age,gender=gender,email=email,aadhar=aadhar,vaccinename= vaccine,zone=zone,location=location,dose=dose,time=time)
        a.save()


        return render(request,"registration2.html", {"messages":"registered!"})

    else:
         return render (request,'registration2.html')
