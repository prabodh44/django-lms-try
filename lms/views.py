from django.shortcuts import render, redirect
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
    # form = CreateEmployee()
    # context = {
    #     'form': form
    # }
    # if (request.method == "POST"):
    #     if form.is_valid():
    #         form.save()
    
    form = CreateStudent()
    print('POST Request', request.POST)
    if(request.method == "POST"):
        print("before is valid method")
        # pass the parameters obtained from the POST request to the form
        # form.is_valid() returns false ASK Alina
        print("FORM Valid", form.is_valid())
        form = CreateStudent(request.POST) 
        # form.save()

        
    return render(request, 'lms/addstudent.html', {'form':form})

def description_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'lms/description.html', {
        'student' : student,
        'student_id' : student_id,
    })
    

    
    
    