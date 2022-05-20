# Generated by Django 4.0.3 on 2022-04-27 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.DateTimeField()),
                ('meetinglocation', models.TextField(blank=True, null=True)),
                ('meetingagenda', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingminutestext', models.TextField(blank=True, null=True)),
                ('meetingattendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meeting')),
            ],
            options={
                'db_table': 'MeetingMinutes',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourceurl', models.URLField()),
                ('resourcedateentered', models.DateField()),
                ('resourcedescription', models.TextField(blank=True, null=True)),
                ('resourcetype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meetingminutes')),
                ('resourceuserid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('eventlocation', models.TextField(blank=True, null=True)),
                ('eventdate', models.DateField()),
                ('eventtime', models.DateTimeField()),
                ('eventdescription', models.TextField(blank=True, null=True)),
                ('eventuserid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]