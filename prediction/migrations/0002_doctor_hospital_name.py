# Generated by Django 3.2.9 on 2021-12-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital_name',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=100, null=True),
        ),
    ]
