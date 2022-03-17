# Generated by Django 3.2.11 on 2022-03-14 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_jobs_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='skills',
            field=models.CharField(choices=[('python', 'python'), ('django', 'django'), ('RESTapi', 'RESTapi'), ('reactjs', 'react'), ('nodejs', 'nodejs'), ('java', 'java'), ('android', 'android')], max_length=200),
        ),
    ]