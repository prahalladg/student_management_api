# Generated by Django 4.1.7 on 2023-03-13 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0007_rename_student_class_name_studentclass_student_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hindi', models.IntegerField()),
                ('english', models.IntegerField()),
                ('math', models.IntegerField()),
                ('science', models.IntegerField()),
                ('sst', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='student.studentinfo')),
                ('std_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='student.studentclass')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='student.studentinfo')),
            ],
        ),
    ]
