# Generated by Django 3.2.5 on 2022-01-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, default='Student', max_length=200, null=True),
        ),
    ]
