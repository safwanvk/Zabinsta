# Generated by Django 3.0.8 on 2020-07-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0012_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
