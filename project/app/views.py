from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound


def index(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def create(request):
    # create_defstudents()

    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        student.lastname = request.POST.get("lastname")
        student.subject_id = request.POST.get("subject")
        student.rating_id = request.POST.get("rating")
        student.average = request.POST.get("average")
        student.save()
        return HttpResponseRedirect('/app')
    defstudents = Student.objects.all()
    return render(request, "create.html", {"defstudents": defstudents})


def edit(request, id):
    try:
        student = Student.objects.get(id=id)

        if request.method == "POST":
            student.name = request.POST.get("name")
            student.lastname = request.POST.get("lastname")
            student.subject_id = request.POST.get("subject")
            student.rating_id = request.POST.get("rating")
            student.average = request.POST.get("average")
            student.save()
            return HttpResponseRedirect('/app')
        else:
            defstudents = Student.objects.all()
            return render(request, "edit.html", {"student": student, "defstudents": defstudents})
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


def delete(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect('/app')
    except Student.DoesNotExis:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


def create_subject():
    if Subject.objects.all().count() == 0:
        Subject.objects.create(name="Русский")


def create_rating():
    if Rating.objects.all().count() == 0:
        Rating.objects.create(number="5")


def create_defstudents():
    if Student.objects.all().count() == 0:
        Student.objects.create(name="Matthew")
        Student.objects.create(lastname="Young")
        Student.objects.create(subject="Математика")
        Student.objects.create(rating="5")
        Student.objects.create(average="5")