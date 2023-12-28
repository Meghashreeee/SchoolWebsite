from django.shortcuts import render,HttpResponse

# Create your views here.
app_name = 'mainapp'
def home(request):
    return render(request,'base.html')

