from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from SchoolSite.settings import EMAIL_HOST_USER
# Create your views here.
app_name = 'mainapp'
def home(request):
    return render(request,'mainapp/home.html')

def about(request):
    return render(request,'mainapp/about.html')

def contact(request):
    return render(request,'mainapp/contact.html')

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
        return render(request,'mainapp/home.html')
    return HttpResponse(status=404)

