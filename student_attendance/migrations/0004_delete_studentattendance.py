# Generated by Django 4.1.7 on 2023-03-21 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0003_rename_studentattendancedetails_studentattendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentAttendance',
        ),
    ]
