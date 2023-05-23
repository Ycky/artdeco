# Generated by Django 4.2.1 on 2023-05-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ART', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='time_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]