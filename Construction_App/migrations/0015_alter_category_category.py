# Generated by Django 4.1.5 on 2024-04-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0014_worker_registration_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]