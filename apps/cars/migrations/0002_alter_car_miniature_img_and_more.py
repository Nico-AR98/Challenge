# Generated by Django 4.1 on 2022-10-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='miniature_img',
            field=models.ImageField(upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='description',
            name='illustrative_img',
            field=models.ImageField(upload_to='cars/'),
        ),
    ]
