# Generated by Django 4.2.4 on 2023-09-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('qulification', models.TextField()),
                ('resume', models.FileField(upload_to='')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('skills', models.CharField(max_length=400)),
                ('places', models.CharField(max_length=250)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
