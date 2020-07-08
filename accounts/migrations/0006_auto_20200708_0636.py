# Generated by Django 3.0.8 on 2020-07-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(default=True, related_name='followed_by', to='accounts.Profile'),
        ),
    ]