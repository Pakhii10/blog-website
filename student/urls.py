from django.urls import path
from student import views
urlpatterns = [
    path('all/',views.all_data,name='all_data'),
    path('blog/',views.blog,name='blog'),
    path('getstart/',views.getstarted,name='getstarted'),
    path('blog/login/',views.loginpage,name='loginpage'),
    path('blog/login/success/',views.success,name='success')
]
