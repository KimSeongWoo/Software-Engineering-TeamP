# Generated by Django 2.2.2 on 2019-06-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0004_auto_20190603_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='changed_password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
