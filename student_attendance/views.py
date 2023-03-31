from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import AllStudentAttendance
from .models import StudentAttendance
from student.models import StudentInfo,StudentClass
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
import json
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def addAttendance(request):
	'''Here we add addtendance to student '''
	attendance_details=AllStudentAttendance()
    
	if request.method == "POST":
		attendance_details=AllStudentAttendance(request.POST)
		student_name = request.POST.get('student_name')
		print(student_name)
		date = request.POST.get('date')
		data_exist= StudentAttendance.objects.filter(student_name=student_name ,date=date).exists()
		print(data_exist)
		if not(data_exist):
			if attendance_details.is_valid():
				attendance_details.save()
				return redirect('/studentattendance/viewattendance')
			else:
				print(attendance_details.errors)
		else:
			messages.error(request,"Data Already Exist")
			
	return render(request,'student_attendance/add_attendance.html',context={"attendance_details":attendance_details})

@login_required
def viewattendance(request):
	'''display all attendance of student'''

	attendancedata = StudentAttendance.objects.all().order_by('student_class','date')
	
	count_attendance=StudentAttendance.objects.values('attendance').order_by().annotate(Count('attendance'))
	print(count_attendance)
	total_present=count_attendance[1]['attendance__count']                    #to count present
	template = loader.get_template('student_attendance/display_attendance.html')
	context={'attendancedata':attendancedata,'total_present':total_present}
	return HttpResponse(template.render(context, request))

@login_required
def editattendance(request,student_id):
	'''Here we edit the attendance and update '''

	attendance_data=StudentAttendance.objects.get(pk=student_id)
	form=AllStudentAttendance(instance=attendance_data)
	if request.method == "POST":
		form = AllStudentAttendance(request.POST ,instance=attendance_data)
		if form.is_valid():
			form.save(commit=True)
			messages.success(request, "updated successfully." )
			return viewattendance(request)
		else:
			print(form.errors)
		messages.error(request,form.errors,"Invalid ") 
	diction={'edit_attendance':form}
	return render(request,'student_attendance/edit_attendance.html',context=diction)


@login_required
def deleteattendance(request,student_id):
	'''Here we delete the marks'''

	attendance=StudentAttendance.objects.get(pk=student_id)
	print(attendance)
	attendance.delete()
	messages.success(request, "Deleted successfully." )
	return redirect('/studentattendance/viewattendance')


@login_required
def load_names(request):
    # attendance_details=AllStudentAttendance(request.POST)
    data = json.loads(request.body)
    cls=data['id']
    name = StudentInfo.objects.filter(std_class=cls)
    return JsonResponse(list(name.values("id","name")), safe=False)
    

