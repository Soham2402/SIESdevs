# Generated by Django 3.2.5 on 2021-09-25 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_proile_image_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, max_length=500, null=True)),
                ('is_read', models.BooleanField(blank=True, default=False, null=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]