# Generated by Django 4.1.6 on 2023-02-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("propertyManager", "0010_alter_propertydetail_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propertydetail",
            name="email",
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
