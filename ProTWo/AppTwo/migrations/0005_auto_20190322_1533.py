# Generated by Django 2.1.7 on 2019-03-22 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0004_auto_20190322_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='username',
            new_name='user',
        ),
    ]