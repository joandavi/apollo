# Generated by Django 2.1.2 on 2018-10-29 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('polls', '0009_auto_20181029_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcvote',
            name='name',
        ),
        migrations.RemoveField(
            model_name='yesnovote',
            name='name',
        ),
        migrations.AddField(
            model_name='mcvote',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.Session'),
        ),
        migrations.AddField(
            model_name='numberedvote',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.Session'),
        ),
        migrations.AddField(
            model_name='yesnovote',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.Session'),
        ),
    ]
