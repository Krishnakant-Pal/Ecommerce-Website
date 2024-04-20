# Generated by Django 4.1.7 on 2024-04-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_bidding_id_alter_comment_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("T", "Toys"),
                    ("H&K", "Home & Kitchen"),
                    ("Clo", "Clothing"),
                    ("B", "Books"),
                    ("Elec", "Electronics"),
                ],
                max_length=5,
                null=True,
            ),
        ),
    ]
