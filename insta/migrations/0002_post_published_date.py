# Generated by Django 3.0.8 on 2020-07-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
