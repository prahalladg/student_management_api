# Generated by Django 4.1.7 on 2023-03-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_rename_student_class_name_studentclass_student_class_and_more'),
        ('student_marks', '0004_remove_subjectmarks_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmarks',
            name='std_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='student.studentclass'),
        ),
    ]
