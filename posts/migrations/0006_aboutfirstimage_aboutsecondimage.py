# Generated by Django 4.1.7 on 2023-04-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFirstImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutSecondImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]