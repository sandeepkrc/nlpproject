# Generated by Django 3.1.7 on 2021-04-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlpapp', '0002_auto_20210411_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('careerp', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='InternShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=20)),
                ('cover', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]