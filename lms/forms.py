from django import forms
from lms.models import Student, Book

class CreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class django_CreateStudent(forms.Form):
    student_name    = forms.CharField()
    student_address = forms.CharField()
    student_phone   = forms.CharField()
    

class CreateEmployee(forms.Form):
    employee_name    = forms.CharField()
    employee_address = forms.CharField()
    employee_phone   = forms.CharField()
    
        