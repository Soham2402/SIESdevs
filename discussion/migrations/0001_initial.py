# Generated by Django 3.2.5 on 2022-01-17 14:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionPost',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('total_vote', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('tags', models.ManyToManyField(blank=True, to='discussion.Type')),
            ],
        ),
    ]
