from django.contrib import messages, sessions
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from app.models import CollegeModel

class Register(CreateView):
    model = CollegeModel
    fields = '__all__'
    template_name = 'registration.html'
    success_url = '/login/'


def login(request):
    try:
        value=request.session['email']
        res = CollegeModel.objects.get(email=value)
        return render(request,'home.html',{"data":res})
    except:
        return render(request, 'login.html')



def logincheck(request):
    e=request.POST["email"]
    p=request.POST['password']
    try:
        CollegeModel.objects.get(email=e,password=p)
        res=CollegeModel.objects.get(email=e)
    except CollegeModel.DoesNotExist:
        messages.error(request,'Details Not Found Please Register and Login')
        return redirect('main')
    else:
        request.session['email'] = e

        return render(request,"home.html",{"data":res})


def home(request):

    return render(request,"home.html")


def logout(request):
    try:
        del request.session['email']
        return login(request)
    except KeyError:
        return redirect("login")