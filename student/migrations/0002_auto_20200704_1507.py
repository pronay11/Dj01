# Generated by Django 2.2.5 on 2020-07-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='GPA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='address',
            field=models.CharField(default=False, max_length=250),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='description',
            field=models.TextField(default=False),
        ),
    ]
