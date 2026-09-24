from django.shortcuts import render, redirect
from .models import Student, StudentDetail
from .forms import StudentForm, StudentListForm

def about(request):
    return render(request, 'about.html')

def student_list(request):
    s = StudentDetail.objects.all()
    return render(request, 'student_list.html', {'students': s})

