from django.db import models

# Create your models here.
class Student(models.Model):
    student_name        = models.CharField(max_length=200)
    student_address     = models.CharField(max_length=200)
    student_department  = models.CharField(max_length=200)
    
    def __str__(self):
        return self.student_name
        
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book_name
    
    

    
    
    
