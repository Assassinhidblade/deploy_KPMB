from django.shortcuts import render
from Registration.models import Course,Student

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render (request, 'index.html')


#course
def new_course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data=Course(code=c_code, description=c_desc)
        data.save()
        dict = {
            'message' : 'Data Save'
        }
    else :
        dict = {
            'message' : ''
        }

    return render (request, 'new_course.html', dict)

def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse': allcourse
    }
    return render (request,'course.html',dict)

def search_course(request):
    if request.method != 'GET':
        return render (request, 'search_course.html')
    
    elif request.method == 'GET':
        data = Course.objects.filter(code = request.GET.get('c_code'))
        data2 = data.count()
        dict = {
        'data': data,
        'data2': data2
        }
        return render (request, 'search_course.html',dict)

def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request, 'update_course.html',dict)

def save_update_course(request,code):
    c_desc= request.POST['desc']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))



#student
def student(request):
    allStudent=Student.objects.all()
    dict={
        'allStudent': allStudent
    }
    return render (request, 'student.html',dict)

def new_student(request):

    allcourse = Course.objects.all().values()
    dict={
        'allcourse': allcourse
    }

    if request.method == 'POST':
        s_id = request.POST['id']
        s_name = request.POST['name']
        s_address = request.POST['address']
        s_phone = request.POST['phone']
        s_course = request.post['course']
        s_code = Course.objects.get(code=s_course)


        data=Student(id=s_id, name=s_name, address=s_address, phone=s_phone, course = s_code)
        data.save()
        dict = {
            'allcourse': allcourse,
            'message' : 'Data Save'
        }
    else :
        dict = {
            'allcourse': allcourse,
            'message' : ''
        }

    return render (request, 'new_student.html',dict)

