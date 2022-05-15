# Generated by Django 4.0.3 on 2022-05-15 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeresourcename', models.CharField(max_length=255)),
                ('typeresourcedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ResourceType',
            },
        ),
        migrations.AlterField(
            model_name='resource',
            name='resourcetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.typeresource'),
        ),
    ]
