# Generated by Django 5.1.5 on 2025-02-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_application_delete_employmentapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='city',
            field=models.CharField(choices=[('porharcourt', 'porharcourt'), ('Bori', 'Bori'), ('logos', 'lagos'), ('Houston', 'Houston')], max_length=255),
        ),
    ]
