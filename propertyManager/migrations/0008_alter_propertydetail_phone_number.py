# Generated by Django 4.1.6 on 2023-02-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("propertyManager", "0007_alter_propertydetail_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propertydetail",
            name="phone_number",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
