# Generated by Django 3.2.5 on 2021-07-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20210708_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedwork',
            name='status',
            field=models.CharField(choices=[('1', 'Assigned'), ('2', 'In Progress'), ('3', 'On Hold'), ('0', 'Completed'), ('-1', 'Layoff')], max_length=15),
        ),
    ]