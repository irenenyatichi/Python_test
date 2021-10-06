# Generated by Django 3.2.7 on 2021-10-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn', '0004_remove_user_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogIn.project')),
                ('simulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogIn.simulation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogIn.user')),
            ],
        ),
    ]
