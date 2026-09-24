from django.contrib import admin
from .models import Student, StudentDetail

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'place']

@admin.register(StudentDetail)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'valid', 'image']