from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from my_code import settings
from django.contrib.auth import authenticate, login, logout
from authentication.models import Info;
from authentication.models import review;
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")

        return redirect('signin')
        
        
    return render(request, "authentication/signup.html")


def signin(request):
    title='Code with harry';
    sus='2+ Million';
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            print('success')
            return render(request, "authentication/homepage.html",{"fname":fname, 'title':title,'sus':sus})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")


def handellogout(request):
     logout(request);
     print('succes fully logout')
     return redirect('home')


def homepage(request):
    title='Code with harry';
    sus='2+ Million';
    
    if request.method =="POST":
        
        comment=request.POST.get('comment');
        type=1;
        if comment !=None: 
         collect=review(comment=comment,type=type);
         collect.save();
        

    des=   reversed(review.objects.filter(type=1));
   
    
    return render(request,'authentication/homepage.html',{'des':des, 'title':title,'sus':sus, }
    );
    
def contact(request):
    success=False;

    if request.method=='POST':
       email=request.POST.get('email');
       comment=request.POST.get('comment');
       
       datasave=Info(email=email,comment=comment);
       datasave.save();
       success=True;

    
    return render(request,'authentication/contact.html',{'success':success,} )
    