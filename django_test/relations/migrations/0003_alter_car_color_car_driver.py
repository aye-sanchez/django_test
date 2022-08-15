# Generated by Django 4.1 on 2022-08-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("relations", "0002_car_owner_age_alter_car_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="car",
                to="relations.colors",
            ),
        ),
        migrations.CreateModel(
            name="Car_driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                (
                    "cars",
                    models.ManyToManyField(related_name="drivers", to="relations.car"),
                ),
            ],
        ),
    ]