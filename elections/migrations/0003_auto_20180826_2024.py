# Generated by Django 2.1 on 2018-08-26 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_auto_20180826_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='cnadidate',
            new_name='candidate',
        ),
    ]
