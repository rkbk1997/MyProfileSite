# Generated by Django 3.1.2 on 2021-08-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfilo', '0003_auto_20210812_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='environment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='project_end_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
