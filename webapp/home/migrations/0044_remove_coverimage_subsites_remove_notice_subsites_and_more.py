# Generated by Django 4.2.16 on 2024-11-11 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_alter_coverimage_auto_full_width'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverimage',
            name='subsites',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='subsites',
        ),
        migrations.DeleteModel(
            name='Subsite',
        ),
    ]
