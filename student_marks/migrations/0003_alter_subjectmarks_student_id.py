# Generated by Django 4.1.7 on 2023-03-13 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_rename_student_class_name_studentclass_student_class_and_more'),
        ('student_marks', '0002_alter_subjectmarks_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo'),
        ),
    ]
