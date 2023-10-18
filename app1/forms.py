from django import forms
from .models import Student, College, Subject

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll_number = forms.CharField(max_length=10)
    college = forms.ModelChoiceField(queryset=College.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
