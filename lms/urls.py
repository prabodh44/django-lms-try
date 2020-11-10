"""skype_first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views




urlpatterns = [
    path('', views.index_view, name='index'),
    path('detail/', views.detail_view, name='detail'),
    path('addstudent/', views.addStudent_view, name='addstudent'),    
    path('addnewbook/', views.addNewBook_view, name='addnewbook'),    
    path('description/<int:student_id>', views.description_view, name='description'),
    path('form/', views.form_view, name='form'),
    path('std/', views.student_view, name='student'),
    path('delete/<int:student_id>', views.delete_student, name='delete'),
    path('update/<int:student_id>', views.update_student, name='update'),
]
