from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
import os
from SchoolSite import settings
from SchoolSite.settings import EMAIL_HOST_USER
from .models import *
# Create your views here.
app_name = 'mainapp'

def home(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/School_images/")
    values = Content.objects.values()
    Announce = Announcement.objects.values()
    faculty_list = faculty.objects.values()
    events_list = Events.objects.values()
    val= {}
    for a in values:
        val[a['Name']] = a['content']
    return render(request,'mainapp/home.html',context={"images": img_list,'content':val,'Announcements':Announce,'faculty':faculty_list,'events':events_list})


def contactform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message= request.POST.get('message')
        print(name,email,message)
        send_mail(
            'Subject here',
            "Name: "+name+"\nEmail: "+email+"\nmessage: "+message,
            EMAIL_HOST_USER,
            ['helloitsme9254@gmail.com','manojpatil9147@gmail.com'],
            fail_silently=False,
        )
        return JsonResponse({'status':'success'})
    return HttpResponse(status=404)