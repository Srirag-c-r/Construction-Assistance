# Generated by Django 4.1.5 on 2023-03-04 10:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Construction_App', '0002_user_reg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_reg',
            new_name='Contractor_Registration',
        ),
    ]