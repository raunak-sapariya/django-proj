from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from utils.strict_gpt import strict_output 
from utils.getImage import getImage
import json


def home(req):
    return render(req,'home.html',{}) 

def allCourses(req):
    return render(req,"courses.html",{"courses":[{'name':'hi'}]})

def addCourse(req):
    return render(req,"addCourse.html",{})

def processAddCourse(req):
    courseName=req.POST.get("courseName")
    unitNames=req.POST.getlist("unitNames")
    units=[]    
    for unit in unitNames:
        prompt="It is your job to create a course about "+unit+", the User has requested to create chapters for each of the units. Then for each chapter, provide a detailed youtube search query that can be used to find informative educational video for each chapter. Each query should give an educational informative course in youtube"
        units.append(prompt)
        
    res=strict_output("You are an AI capable of curating course content, coming up with relevant chapter titles related to given by user, and finding relevant youtube videos title for each chapter",
    units,
    {
        "title":"title of unit",
        "chapter":"an array of at least 5 chapters, each chapter should have a youtube search query  and a chapter title key in the JSON object",
    })
    res=json.loads(res) 
    image=getImage(courseName)
    return render(req,"course.html",{"courses":res})

def course(req,courseId):
    print(res)
    return render(req,"course.html",{"courses":res})

def loginUser(req):
    pass


def logoutUser(req):
    pass


