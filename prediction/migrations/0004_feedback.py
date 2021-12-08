# Generated by Django 3.2.9 on 2021-12-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_alter_doctor_hospital_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
                ('happy', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
