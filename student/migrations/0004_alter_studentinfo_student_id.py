# Generated by Django 4.1.7 on 2023-03-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_studentinfo_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
