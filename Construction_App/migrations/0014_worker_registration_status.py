# Generated by Django 4.1.5 on 2023-05-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0013_request_status1'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker_registration',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]