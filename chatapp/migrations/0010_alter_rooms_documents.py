# Generated by Django 5.1.2 on 2025-01-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatapp", "0009_rooms_documents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rooms",
            name="documents",
            field=models.FileField(blank=True, null=True, upload_to="filesd"),
        ),
    ]
