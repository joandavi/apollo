# Generated by Django 2.1.2 on 2018-10-24 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_auto_20181022_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=16)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Room')),
            ],
        ),
        migrations.CreateModel(
            name='MCVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NumberedVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='YesNoVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='choice',
        ),
        migrations.AddField(
            model_name='option',
            name='poll',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Type'),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.AddField(
            model_name='yesnovote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AddField(
            model_name='yesnovote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='numberedvote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AddField(
            model_name='numberedvote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mcvote',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Option'),
        ),
        migrations.AddField(
            model_name='mcvote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AddField(
            model_name='mcvote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
