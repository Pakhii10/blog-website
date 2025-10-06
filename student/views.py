from django.shortcuts import render
from student.models import Profile
from student.forms import LoginForm , blogform
from django.http import HttpResponseRedirect

# Create your views here.
def all_data(req):
    
    stu=Profile.objects.all()
    print(stu)
    return render(req,'student/home.html',{'showstu':stu})

def blog(req):
    return render(req,'student/bloghome.html')

def getstarted(req):
    fm=blogform()
    return render(req,'student/getstart.html',{'form':fm})

def loginpage(req):
   if req.method == "POST":
        lg=LoginForm(req.POST)
        if lg.is_valid():
            lg.save()
            return render(req,'student/success.html')
   else:
        lg=LoginForm()
   return render(req,'student/login.html',{'loginform':lg})

def success(req):
    return render(req,'student/success.html')