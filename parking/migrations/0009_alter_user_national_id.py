# Generated by Django 5.1.7 on 2025-04-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0008_remove_reservation_garage_alter_parkingslot_garage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
