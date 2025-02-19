# Generated by Django 4.1.5 on 2023-04-21 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Construction_App', '0007_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='con_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200, null=True)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Construction_App.contractor_registration')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Construction_App.worker_registration')),
            ],
        ),
    ]
