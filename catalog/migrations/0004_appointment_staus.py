# Generated by Django 3.1.12 on 2022-01-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20220112_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='staus',
            field=models.BooleanField(default=False),
        ),
    ]
