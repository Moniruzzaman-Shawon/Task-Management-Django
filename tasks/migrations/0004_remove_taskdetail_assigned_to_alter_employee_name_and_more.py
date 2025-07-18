# Generated by Django 5.2.3 on 2025-07-06 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_taskdetail_notes_alter_taskdetail_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskdetail',
            name='assigned_to',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='details', to='tasks.task'),
        ),
    ]
