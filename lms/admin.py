from django.contrib import admin

from lms.models import Student, Book, Employee

# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Employee)
