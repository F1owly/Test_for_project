# Generated by Django 5.0.1 on 2024-02-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_room_number_of_room_alter_room_type_of_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Number_of_room',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='Type_of_room',
            field=models.IntegerField(),
        ),
    ]
