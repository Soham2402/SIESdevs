# Generated by Django 3.2.5 on 2021-09-14 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['date_created']},
        ),
    ]
