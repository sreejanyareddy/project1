# Generated by Django 5.0.6 on 2024-06-23 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('days', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Superadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('username', models.CharField(default=' ', max_length=255)),
                ('password', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('curCode', models.CharField(default='None', max_length=10)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.classes')),
            ],
        ),
        migrations.CreateModel(
            name='CountClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.course')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='curCourses',
            field=models.ManyToManyField(blank=True, related_name='assigned_class', to='application.course'),
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
                ('allPeriods', models.ManyToManyField(to='application.period')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.slot'),
        ),
        migrations.AddField(
            model_name='classes',
            name='availableSlots',
            field=models.ManyToManyField(blank=True, related_name='classes', to='application.slot'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('username', models.CharField(default=' ', max_length=255)),
                ('password', models.CharField(default='', max_length=15)),
                ('class_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent')], max_length=10)),
                ('codeEntered', models.CharField(max_length=10)),
                ('deviceId', models.CharField(default='', max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.course')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='application.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('username', models.CharField(default=' ', max_length=255)),
                ('password', models.CharField(default='', max_length=15)),
                ('curCourses', models.ManyToManyField(blank=True, related_name='assigned_teachers', to='application.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(blank=True, related_name='courses', to='application.teacher'),
        ),
    ]
