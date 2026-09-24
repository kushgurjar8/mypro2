from django import forms
from .models import Student, StudentDetail

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'place']

class StudentListForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ['name', 'valid', 'image']