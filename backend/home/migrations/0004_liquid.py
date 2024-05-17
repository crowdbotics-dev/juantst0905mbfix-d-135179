# Generated by Django 3.2.25 on 2024-05-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_solid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Liquid",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
            ],
        ),
    ]
