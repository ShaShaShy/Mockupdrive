# Generated by Django 4.0.5 on 2022-10-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=200, null=True)),
                ('fileUp', models.FileField(upload_to='media/')),
                ('fileType', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]