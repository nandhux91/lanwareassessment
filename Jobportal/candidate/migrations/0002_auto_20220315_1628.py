# Generated by Django 3.2.11 on 2022-03-15 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_jobs_skills'),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.jobs'),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='experience',
            field=models.PositiveIntegerField(max_length=250),
        ),
    ]
