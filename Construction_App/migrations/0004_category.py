# Generated by Django 4.1.5 on 2023-03-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0003_rename_user_reg_contractor_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
