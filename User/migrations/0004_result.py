# Generated by Django 4.1 on 2022-09-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_student_first_name_alter_student_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('totalmarks', models.CharField(max_length=100)),
            ],
        ),
    ]
