# Generated by Django 4.2.6 on 2023-10-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_task', '0004_alter_mytask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytask',
            name='status',
            field=models.CharField(choices=[('', 'Select Status'), ('inprogress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=20),
        ),
    ]
