# Generated by Django 4.2.4 on 2023-09-05 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_jobseeker_qulification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='specializations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_list', to='account.specialization'),
        ),
    ]