# Generated by Django 4.0.5 on 2022-10-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_userupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userupload',
            name='fileUp',
            field=models.FileField(upload_to='media'),
        ),
    ]
