# Generated by Django 5.0.1 on 2024-01-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_room_type_of_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Number_of_room',
            field=models.CharField(default=2, max_length=3),
            preserve_default=False,
        ),
    ]
