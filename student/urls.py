from django.urls import path
from student import views
urlpatterns = [
    path('all/',views.all_data,name='all_data'),
    path('blog/',views.blog,name='blog'),
    path('getstart/',views.getstarted,name='getstarted'),
    path('blog/reglogin/',views.register,name='regloginpage'),
    path('blog/reglogin/success/',views.success,name='success'),
    path('reglogin/loginpage/',views.login,name='loginpage'),
    path('logout/', views.logout, name='logout'),  
]
