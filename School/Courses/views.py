from django.shortcuts import render
from .models import Course
from django.db.models import Q,Value,CharField
import re
from django.db.models.functions import Concat

# Create your views here.
def Welcome_View(request):
    name="Hussein Abaza"
    return render(request,"Courses/Welcome.html",{"name":name})

def Courses_Info(request):
    if request.GET.get('search'):
        search=request.GET.get('search')
        course_list=Course.objects.annotate(
            name=Concat('course_name', Value(' '), 'course_number',output_field=CharField())
        ).filter(name__icontains=search)
        context = {"course_list": course_list}
    else:
        context={"course_list":Course.objects.all()}
    return render(request,"Courses/List_Courses.html",context)
