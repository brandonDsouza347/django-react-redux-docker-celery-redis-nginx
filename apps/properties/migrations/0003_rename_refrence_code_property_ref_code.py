# Generated by Django 5.0.2 on 2024-02-15 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0002_rename_slud_property_slug_alter_property_photo1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="property",
            old_name="refrence_code",
            new_name="ref_code",
        ),
    ]
