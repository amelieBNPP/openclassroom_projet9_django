# Generated by Django 3.2.4 on 2021-09-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210817_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='database/statics/images/',
            ),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
