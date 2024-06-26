# Generated by Django 5.0.1 on 2024-05-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0004_alter_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
