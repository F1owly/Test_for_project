# Generated by Django 5.0.1 on 2024-02-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_alter_room_number_of_room_alter_room_type_of_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('role', models.IntegerField()),
            ],
        ),
    ]