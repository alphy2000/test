# Generated by Django 5.1.3 on 2024-11-11 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('person', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.IntegerField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.industry')),
            ],
        ),
    ]
