from django.shortcuts import render,HttpResponse,redirect
import json
from django.contrib.auth.models import User,auth
import re
# Create your views here.

def register(req):
    
    if req.method =='POST':
       
       
       
       username=req.POST['f_name']
       email=req.POST['mail']
       password=req.POST['pass']
       print(email)

       regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
       if not (re.fullmatch(regex,email)):
           req.session['error']="Incorrect email"
           return redirect("/register")
        
     


      


       if User.objects.filter(username=username).exists():
          print("taken")
          req.session['error']="Username already taken"
          return redirect("/register")
          
       if User.objects.filter(email=email).exists():
          print("email taken")
          req.session['error']="Email already taken"
          return redirect("/register")
         
       else:   
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        
       return render(req,'home.html')
    
    
    else:
     error=req.session.get("error","")
     req.session['error']=''
     return render(req,'registration/register.html',{"error":error})

def login(req):
    print(req.method)
   
    return render(req,'registration/login.html')






