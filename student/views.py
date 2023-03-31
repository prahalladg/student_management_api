from django.shortcuts import render
from .models import StudentInfo
from .forms import NewStudentForm
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def addstudent(request):
	''' Here we will add new student '''

	if request.method == "POST":
		users_form = NewStudentForm(request.POST)
		if users_form.is_valid():
			users_form.save()
			messages.success(request, "Added student successful." )
			return redirect('/student')
		else:
			print(users_form.errors)
		messages.error(request,users_form.errors,"Invalid ") 
	users_form=NewStudentForm()
	return render(request,'student/addstudent.html',context={"add":users_form})

@login_required
def viewstudent(request):
	'''here we will view all the student details'''

	studentdata = StudentInfo.objects.all().order_by("std_class")
	template = loader.get_template('student/studentDetails.html')
	context={'studentdata':studentdata}
	return HttpResponse(template.render(context, request))

@login_required
def editstudent(request,student_id):
	'''Here we will edit the particular student through student_id'''

	student_data=StudentInfo.objects.get(pk=student_id)
	form=NewStudentForm(instance=student_data)
	if request.method == "POST":
		form = NewStudentForm(request.POST ,instance=student_data)
		if form.is_valid():
			form.save(commit=True)
			messages.success(request, "updated successfully." )
			return viewstudent(request)
		else:
			print(form.errors)
		messages.error(request,form.errors,"Invalid ") 
	diction={'edit_student':form}
	return render(request,'student/editstudent.html',context=diction)

@login_required
def deletestudent(request,student_id):
	'''Here we will delete the particular student details through student_id'''
	student=StudentInfo.objects.get(pk=student_id)
	student.delete()
	messages.success(request, "Deleted successfully." )
	return redirect('/student/viewstudent')
	