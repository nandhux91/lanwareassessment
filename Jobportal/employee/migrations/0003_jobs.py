# Generated by Django 3.2.11 on 2022-03-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220314_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(choices=[('python', 'python'), ('django', 'django'), ('REST api', 'REST api'), ('reactjs', 'react'), ('nodejs', 'nodejs'), ('java', 'java'), ('android', 'android')], max_length=200)),
                ('salary', models.PositiveIntegerField(max_length=200, null=True)),
                ('posted_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]