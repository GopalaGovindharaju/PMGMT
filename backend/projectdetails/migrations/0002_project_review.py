# Generated by Django 4.2.5 on 2023-11-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectdetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Review',
            field=models.IntegerField(default=0),
        ),
    ]