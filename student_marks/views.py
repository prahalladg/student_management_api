from django.shortcuts import render
from .models import SubjectMarks
from .forms import studentMarksForm
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.core.mail import send_mail
from student.models import StudentInfo
from django.contrib.auth.decorators import login_required

@login_required
def addMarks(request):
	'''Here we add all marks of student and send mail to student '''
	if request.method == "POST":
		sname=request.POST.get('student_name')
		hindi=request.POST.get('hindi')
		english=request.POST.get('english')
		math=request.POST.get('math')
		science=request.POST.get('science')
		sst=request.POST.get('sst')
		total=int(hindi)+int(english)+int(math)+int(science)+int(sst)
		percentage=int(total) / 500 * 100
		
		marks_form = studentMarksForm(request.POST)
		student_data=StudentInfo.objects.get(id=sname)
		stud_mail=student_data.email
		stud_name=student_data.name
		stud_id=student_data.student_id
		stud_class=student_data.std_class


		if marks_form.is_valid():
			marks_form.save()
			mailbody=f"Student Name: {stud_name}\n Student ID:{stud_id}\n Class:{stud_class}\n Here is the marks details \n \n Hindi:{hindi}\n English:{english}\n Math:{math}\n Science:{science}\n SST:{sst}\n Total:{total}\n Percentage:{percentage}% "


			send_mail(f'{"marks"}',f'{mailbody}','info@laps.com',[f'{stud_mail}'],fail_silently=False)
			print(total)
			messages.success(request, "Added marks successful." )
			return redirect('/studentmarks/viewmarks')
		else:
			print(marks_form.errors)
		messages.error(request,marks_form.errors,"Invalid ") 
	marks_form=studentMarksForm()
	return render(request,'marks/addmarks.html',context={"addmarks":marks_form})

@login_required
def viewmarks(request):
	'''display all marks of student'''

	marksdata = SubjectMarks.objects.all()
	template = loader.get_template('marks/viewmarks.html')
	context={'marksdata':marksdata}
	return HttpResponse(template.render(context, request))

@login_required
def editmarks(request,student_id):
	'''Here we edit the marks and update '''

	marks_data=SubjectMarks.objects.get(pk=student_id)
	form=studentMarksForm(instance=marks_data)
	if request.method == "POST":
		form = studentMarksForm(request.POST ,instance=marks_data)
		if form.is_valid():
			form.save(commit=True)
			messages.success(request, "updated successfully." )
			return viewmarks(request)
		else:
			print(form.errors)
		messages.error(request,form.errors,"Invalid ") 
	diction={'edit_marks':form}
	return render(request,'marks/edit_marks.html',context=diction)

@login_required
def deletemarks(request,student_id):
	'''Here we delete the marks'''

	student=SubjectMarks.objects.get(pk=student_id)
	print(student)
	student.delete()
	messages.success(request, "Deleted successfully." )
	return redirect('/studentmarks/viewmarks')

