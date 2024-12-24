from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.base, name='base'),
    path('base/', views.home, name='base'),
    path('singup/',views.singup,name='singup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('clubs/', views.club_list, name='club_list'),
    path('books/', views.book_list, name='book_list'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('new-password/', views.new_password, name='new_password'),
   
]

