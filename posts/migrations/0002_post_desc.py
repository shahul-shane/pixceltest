# Generated by Django 4.1.7 on 2023-04-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]