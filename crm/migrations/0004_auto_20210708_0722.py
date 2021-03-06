# Generated by Django 3.2.5 on 2021-07-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_workassigned_assignedwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedwork',
            name='status',
            field=models.CharField(choices=[('1', 'Assigned'), ('2', 'In Progress'), ('3', 'On Hold'), ('0', 'Completed')], max_length=15),
        ),
        migrations.AlterField(
            model_name='assignedwork',
            name='updated_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
