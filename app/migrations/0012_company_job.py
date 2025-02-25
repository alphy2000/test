# Generated by Django 5.1.3 on 2024-11-12 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_job_companyname_delete_company_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('person', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('whatsapp', models.CharField(max_length=15, null=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.industry')),
                ('userdet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usersignup')),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
                ('location', models.CharField(max_length=500)),
                ('jobtype', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract')], default='Full Time', max_length=1000)),
                ('hours', models.IntegerField()),
                ('days', models.IntegerField()),
                ('minsalary', models.CharField(max_length=15)),
                ('maxsalary', models.CharField(max_length=15)),
                ('qualification', models.CharField(max_length=500)),
                ('skills', models.CharField(max_length=500)),
                ('experience', models.IntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Any', 'Any')], default='Any', max_length=1000)),
                ('minage', models.IntegerField(null=True)),
                ('maxage', models.IntegerField(null=True)),
                ('approval', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=1000)),
                ('companyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]
