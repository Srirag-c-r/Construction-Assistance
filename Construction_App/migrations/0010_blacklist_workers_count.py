# Generated by Django 4.1.5 on 2023-04-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0009_con_feedback_reply_feedback_reply_blacklist_workers'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist_workers',
            name='count',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
