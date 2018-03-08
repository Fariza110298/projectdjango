from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from teacher.models import Teacher, Students
# Create your views here.

def basic_one(request):
    view="basic_one"
    html="<html><body>This is %s view</html></body>" %view
    return HttpResponse(html)

def template_two(request):
    view="template_two"
    t=get_template('myview.html')
    html=t.render({'name':view})
    return HttpResponse(html)

def template_three_simple(request):
    view="template_three"
    return render_to_response('myview.html', {'name':view})

def teachers(request):
    return render_to_response('teachers.html', {'teachers': Teacher.objects.all()})

def students(request):
    return render_to_response('studentts.html', {'students': Students.objects.all()})
