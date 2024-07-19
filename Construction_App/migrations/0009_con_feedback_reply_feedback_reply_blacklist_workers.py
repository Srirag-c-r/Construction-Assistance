# Generated by Django 4.1.5 on 2023-04-23 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0008_con_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='con_feedback',
            name='reply',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='reply',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Blacklist_workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200, null=True)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Construction_App.contractor_registration')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Construction_App.worker_registration')),
            ],
        ),
    ]