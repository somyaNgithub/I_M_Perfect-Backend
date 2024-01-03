# Generated by Django 4.2.5 on 2024-01-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0004_passwordresettoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='categories',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fullName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobileNo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userName',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
