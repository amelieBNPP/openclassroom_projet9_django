# Generated by Django 3.2.4 on 2021-09-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='../static/images/',
            ),
        ),
    ]
