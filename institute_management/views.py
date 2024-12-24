from django.shortcuts import render , redirect
from .models import User , Student, Teacher, Club, Book
from django.core.mail import send_mail
from django.conf import settings
import random


def base(request):
    return render(request, 'base.html')

def home(request):
    
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    club_count = Club.objects.count()
    book_count = Book.objects.count()

   
    context = {
        'student_count': student_count,
        'teacher_count': teacher_count,
        'club_count': club_count,
        'book_count': book_count,
    }
    return render(request, 'base.html', context)
     # return render(request, 'base.html')


def singup(request):
    if request.method == "POST":
        try:
            # Check if the email is already registered
            User.objects.get(email=request.POST['email'])
            msg = "Email already registered"
            return render(request, 'singup.html', {'msg': msg})
        except User.DoesNotExist:
            # Check if the passwords match
            if request.POST['password'] == request.POST['cpassword']:
                # Create a new user
                user = User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture']
                )
                # Save user details in the session
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                # Redirect to base.html
                return redirect('base')  # Ensure 'base' URL name is defined in your URLs
            else:
                msg = "Password & confirm password do not match"
                return render(request, 'singup.html', {'msg': msg})
    else:
        return render(request, 'singup.html')



# def login(request):
#     if request.method=="POST":
#         try:
#             user=User.objects.get(email=request.POST['email'])
#             if user.password==request.POST['password']:
#                 request.session['email']=user.email
#                 request.session['fname']=user.fname
#                 return render(request,'index.html')
#             else:
#                 msg="Incorrect password"
#                 return render(request,'login.html',{'msg':msg})
#         except:
#             msg="Email not Register"
#             return render(request,'login.html',{'msg':msg})
#     else:
#         return render(request,'login.html')

from django.shortcuts import redirect

def login(request):
    if request.method == "POST":
        try:
            # Retrieve user by email
            user = User.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                # Save user details in session
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                request.session['profile_picture'] = user.profile_picture.url
                # Redirect to base.html
                return redirect('base')  # Ensure 'base' URL name exists in urls.py
            else:
                msg = "Incorrect password"
                return render(request, 'login.html', {'msg': msg})
        except User.DoesNotExist:
            msg = "Email not registered"
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')



# def logout(request):
# 	try:
# 		del request.session['email']
# 		del request.session['fname']
# 		msg="Uaer logout Succesfully"
# 		return render(request,'login.html',{'msg':msg})
# 	except:
# 		msg="Uaer logout Succesfully"
# 		return render(request,'base.html',{'msg':msg})

def logout(request):
    try:
        # Clear session data
        del request.session['email']
        del request.session['fname']
        del request.session['profile_picture']
        msg = "User logged out successfully"
    except KeyError:
        # If session variables are missing, no action needed
        msg = "User logged out successfully"
    # Redirect to login page
    return redirect('login')  # Ensure 'login' URL name exists in urls.py



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})

def book_list(request):
    books = Book.objects.all()


def profile(request):
    try:
        user = User.objects.get(email=request.session['email'])
        return render(request, 'profile.html', {'user': user})
    except User.DoesNotExist:
        return render(request, 'login.html', {'msg': 'User not found'})


def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP for FORGOT PASSWORD'
            message = 'Hello '+user.fname+',Your Otp  is for Forgot password is : '+ str(otp)
            email_from =settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail( subject, message, email_from, recipient_list)
            request.session['otp']=otp
            request.session['email']=user.email
            return render(request,'otp.html')
        except:
            msg="Email not Register"
            return render(request, 'forgot_password.html',{'msg':msg})
    else:
        return render(request, 'forgot_password.html')

     
    
def verify_otp(request):
    otp1=int(request.POST['otp'])
    otp2=int(request.session['otp'])
    if otp1==otp2:
        del request.session['otp']
        return render(request,'new-password.html')
    else:
        msg="invalid otp"
        return render(request, 'otp.html')

def new_password(request):
    if request.POST['new_password']==request.POST['cnew_password']:
        user=User.objects.get(email=request.session['email'])
        user.password=request.POST['new_password']
        user.save()
        del request.session['email']
        msg="Password Change successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="new password and confirom Password Does NOT match"
        return render(request,'new-password.html')





