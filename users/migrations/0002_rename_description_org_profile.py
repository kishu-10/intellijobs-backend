# Generated by Django 3.1.7 on 2022-03-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationprofile',
            name='org_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='organizationprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
