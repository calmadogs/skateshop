# Generated by Django 5.0.2 on 2024-02-21 00:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "polls_skate_parts",
            "0002_alter_skateparts_options_alter_skateparts_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelTable(
            name="skateparts",
            table="skate_part",
        ),
    ]
