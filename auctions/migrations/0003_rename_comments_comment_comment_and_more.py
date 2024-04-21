# Generated by Django 4.1.7 on 2024-04-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0002_listing_alter_user_id_comment_bidding"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="comments",
            new_name="comment",
        ),
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("Elec", "Electronics"),
                    ("B", "Books"),
                    ("H&K", "Home & Kitchen"),
                    ("C", "Clothing"),
                ],
                max_length=5,
                null=True,
            ),
        ),
    ]