# Generated by Django 5.0.2 on 2024-03-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0006_alter_userprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to='chatter.account'),
        ),
    ]
