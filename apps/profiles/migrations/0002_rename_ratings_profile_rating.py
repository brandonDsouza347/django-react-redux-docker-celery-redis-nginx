# Generated by Django 5.0.2 on 2024-02-16 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="ratings",
            new_name="rating",
        ),
    ]