# Generated by Django 3.0.8 on 2020-07-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20200707_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
