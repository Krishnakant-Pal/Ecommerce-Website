# Generated by Django 4.1.7 on 2024-04-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_rename_comments_comment_comment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bidding",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("H&K", "Home & Kitchen"),
                    ("C", "Clothing"),
                    ("Elec", "Electronics"),
                    ("B", "Books"),
                ],
                max_length=5,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]