# Generated by Django 3.2.7 on 2021-10-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('project_name', models.TextField(default='project_name', max_length=50)),
                ('project_description', models.CharField(default='project description', max_length=500)),
                ('simulation_name', models.CharField(default='default simulation', max_length=30)),
            ],
        ),
    ]
