# Generated by Django 4.2.6 on 2023-10-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_task', '0005_alter_mytask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytask',
            name='status',
            field=models.CharField(choices=[('inprogress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=20),
        ),
    ]
