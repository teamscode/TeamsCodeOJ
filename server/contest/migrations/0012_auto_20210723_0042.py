# Generated by Django 2.1.7 on 2021-07-23 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_oicontestrank_last_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oicontestrank',
            name='last_submission',
            field=models.DateTimeField(null=True),
        ),
    ]
