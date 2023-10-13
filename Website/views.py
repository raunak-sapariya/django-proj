from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse,JsonResponse
from django.contrib import messages
from utils.strict_gpt import process_prompt
from utils.getImage import getImage
import concurrent.futures
from django.views.decorators.csrf import csrf_exempt
from .models import Course,Unit,Chapter,Question
import time 
import json
from uuid import uuid4

courses=[]

def home(req):
    return render(req,'home.html',{}) 

def allCourses(req):
    return render(req,"courses.html",{"courses":[{'name':'hi'}]})

def addCourse(req): 
    return render(req,"addCourse.html",{})

def processAddCourse(req):
    data=json.loads(req.body.decode("utf-8"))
    courseName=data.get("courseName")
    unitNames=data.get("units")
    req.session["courseName"]=courseName
    courses.append((courseName,unitNames))
    return JsonResponse({"message":"done"})


    """ units=[]    
    for unit in unitNames:
        prompt="It is your job to create a course about "+unit+", the User has requested to create chapters for each of the units. Then for each chapter, provide a detailed youtube search query that can be used to find informative educational video for each chapter. Each query should give an educational informative course in youtube"
        units.append(prompt)
        
    with concurrent.futures.ThreadPoolExecutor() as exc:
   

        res=[exc.submit(process_prompt,)for prompt in units]

        for f in concurrent.futures.as_completed(res):
            yield f.result()
    """

def streamUnit(req):
    if (len(courses)!=0):
        courseName=courses[0][0]
        unitNames=courses[0][1]
        units=[]
        for unit in unitNames:
            prompt="The User wants to pursue "+ courseName +"It is your job to create a course only about "+unit+", the User has requested to create chapters for each of the units. Then for each chapter, provide a detailed youtube search query that can be used to find informative educational video for each chapter. Each query should give an educational informative course in youtube"
            units.append(prompt)
        
   
        courses.pop(0)

        res=StreamingHttpResponse(streamHelper(units),content_type="text/event-stream")
        
        return res
    return render(req,"addCourse.html")

def streamHelper(units):

    with concurrent.futures.ThreadPoolExecutor() as exc:
        res=[exc.submit(process_prompt,prompt) for prompt in units]
        for f in concurrent.futures.as_completed(res):
            data=json.loads(f.result().replace("'",'"'))
            title=data["title"]
            chapters=data["chapters"]    
            yield f"data:{json.dumps({'title': title, 'chapters': chapters})}\n\n"
        

def generateCourse(req,courseName):
    return render(req,"generateCourse.html",{"courseName":courseName})


def course(req,courseId):

    """ get course by id """


    return render(req,"course.html",{"courses":courseId})



@csrf_exempt
def addCourseToDB(req):

    data=json.loads(req.body.decode("utf-8"))
    courseName=data["courseName"]
    courseImg=getImage(courseName)
    units=data["unitData"]
    
    course=Course(id=str(uuid4()),name=courseName,image=courseImg)
    course.save()
    for unit in units:
        unit=Unit(id=str(uuid4()),name=unit["title"],courseId=course.id,course=course)
        unit.save()
    
    return JsonResponse({"courseID":course.id})
    
    
