# Generated by Django 2.1.7 on 2019-03-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
            ],
        ),
    ]