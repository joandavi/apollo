# Generated by Django 2.1.2 on 2018-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20181025_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yesnovote',
            name='vote',
            field=models.CharField(max_length=5),
        ),
    ]
