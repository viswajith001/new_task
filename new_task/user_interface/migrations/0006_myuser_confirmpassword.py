# Generated by Django 4.2.6 on 2023-10-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0005_alter_myuser_options_alter_myuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='confirmpassword',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]