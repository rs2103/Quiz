# Generated by Django 4.1 on 2022-09-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_rename_subject_name_subject_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addquestion',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]
