# Generated by Django 4.2.4 on 2024-05-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("THMovie", "0004_rename_movie_id_available_movie_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="type",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]