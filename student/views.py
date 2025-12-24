from django.shortcuts import render,redirect
from django.contrib import messages
from student.models import Profile ,UserRegistration,BlogPost
from student.forms import RegistrationForm , blogform ,LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def all_data(req):
    
    stu=Profile.objects.all()
    print(stu)
    return render(req,'student/home.html',{'showstu':stu})

def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # newest first
    return render(request, 'student/bloghome.html', {'posts': posts})

def getstarted(request):
     form = blogform()
     if request.method == "POST":
        form = blogform(request.POST, request.FILES)
        if form.is_valid():
            BlogPost.objects.create(
                title=form.cleaned_data['blog_title'],
                content=form.cleaned_data['blog_description'],
                video=form.cleaned_data['blog_video'],
                author_name=request.session.get('username', 'Anonymous')  # auto from session
            )
            messages.success(request, "Your blog post has been created!")
            return redirect('blog')
        else:
            print("error message")
            form = blogform()
     return render(request, 'student/getstart.html', {'form': form})

# def loginpage(req):
#    if req.method == "POST":
#         lg=LoginForm(req.POST)
#         if lg.is_valid():
#             lg.save()
#             return render(req,'student/success.html')
#    else:
#         lg=LoginForm()
#    return render(req,'student/login.html',{'loginform':lg})

def register(req):
   if req.method == "POST":
        lg=RegistrationForm(req.POST)
        if lg.is_valid():
            lg.save()
            messages.success(req, "Your account has been created! Please log in.")
            return redirect('loginpage')
   else:
        lg=RegistrationForm()
   return render(req,'student/reglogin.html',{'RegistrationForm':lg})

def login(request):
    # if 'username' in request.session:  # ✅ Already logged in
    #     username = request.session['username']
    #     print("Already logged in as:", username)
    #     return redirect('blog')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the username exists in DB
            try:
                user = UserRegistration.objects.get(username=username)
            except UserRegistration.DoesNotExist:
                messages.error(request, "Username not found.")
                return render(request, 'student/loginpage.html', {'form': form})

            # Check password
            if user.password == password:
                # Store login info in session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f"Welcome back, {user.firstname}!")
                return redirect('blog')  # redirect to your success/home page
            else:
                messages.error(request, "Incorrect password.")
    else:
        form = LoginForm()

    return render(request, 'student/loginpage.html', {'form': form})

def logout(request):
    if 'username' in request.session:
        username = request.session['username']
        # messages.success(request, f"{username}, you have been logged out successfully.")
        request.session.flush()  # ✅ Clears all session data
    else:
        messages.info(request, "You are not logged in.")
    return redirect('loginpage')



def success(req):
    return render(req,'student/success.html')