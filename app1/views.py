from .models import Student, College, Subject
from .forms import StudentForm
from django.shortcuts import render, redirect

def student_view(request):
    colleges = College.objects.all()
    subjects = Subject.objects.all()
    student = Student.objects.all()
    print(student.query)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_number = form.cleaned_data['roll_number']
            college = form.cleaned_data['college']
            subject = form.cleaned_data['subject']
            student = Student(name=name, roll_number=roll_number, college=college, subject=subject)
            student.save()
            return redirect('student_view')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'colleges': colleges, 'subjects': subjects,'student':student})