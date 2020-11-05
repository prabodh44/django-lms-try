from django.shortcuts import render
from django.http import HttpResponse

from lms.models import Student, Book
from lms.forms import CreateStudent, django_CreateStudent, CreateEmployee



def index_view(request):
    context = {
        
    }
    return render(request, "lms/index.html", context)

def detail_view(request):
    student_list = Student.objects.all()
    return render(request, 'lms/detail.html', {
        'student_list' : student_list,
    })

def addStudent_view(request):
    form = CreateEmployee()
    context = {
        'form': form
    }
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
        
    return render(request, 'lms/addstudent.html', context)

def description_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'lms/description.html', {
        'student' : student,
        'student_id' : student_id,
    })
    

    
    
    