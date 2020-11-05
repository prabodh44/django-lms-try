from django.db import models

# Create your models here.

# Entities
# Student, Book 

# Student and Book  1 to Many relationship

class Student(models.Model):
    student_name       = models.CharField(max_length=200)
    student_address    = models.CharField(max_length=200)
    student_phone      = models.CharField(max_length=200)
    
    def __str__(self):
        return self.student_name
    
class Book(models.Model):
    book_name       = models.CharField(max_length=1000)
    student         = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_summary    = models.TextField(default='this is a summary')
    
    def __str__(self):
        return self.book_name


class Employee(models.Model):
    employee_name       = models.CharField(max_length=200)
    employee_address    = models.CharField(max_length=200)
    employee_phone      = models.CharField(max_length=200)
        


    


