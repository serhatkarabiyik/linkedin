# Generated by Django 5.1 on 2024-11-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('users', '0002_rename_user_profile_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='skills.skill'),
        ),
    ]
