from django.shortcuts import render
from .models import Student, Grade, Course
from django.http import HttpResponse


def show(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'school/show.html', context)


def content(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'school/content.html', {'student': student})


def search(request):
    if 'q' in request.GET:
        message = request.GET['q']
        all_students = Student.objects.filter(name__contains=message)
        context = {'all_students': all_students}
        return render(request, 'school/show.html', context)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def addstudent(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'school/addStudent.html', context)


def adddstu(request):
    if 'name' in request.GET:
        message = request.GET['name']
        message2 = request.GET['acyear']
        student = Student()
        student.name = message
        student.ac_year = message2
        student.save()
        grade1 = Grade()
        grade1.student = student
        grade1.course = Course.objects.get(pk=2)
        grade1.degree = int(request.GET['degree'])
        grade1.save()
        return content(request, student.pk)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def course(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'school/addCourse.html', context)


def addcourse(request):
    if 'course' in request.GET:
        message = request.GET['course']
        message2 = int(request.GET['max'])
        course1 = Course()
        course1.name = message
        course1.max_degree = message2
        course1.save()
        return show(request)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def students(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'school/Students.html', context)


def deleteStudent(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'school/show.html', context)



