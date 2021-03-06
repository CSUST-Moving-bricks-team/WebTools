# Generated by Django 2.1 on 2019-02-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20190219_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='bronze_num',
            field=models.IntegerField(default=24, verbose_name='铜奖数量'),
        ),
        migrations.AddField(
            model_name='contest',
            name='gold_num',
            field=models.IntegerField(default=8, verbose_name='金奖数量'),
        ),
        migrations.AddField(
            model_name='contest',
            name='problem_num',
            field=models.IntegerField(default=13, verbose_name='题目数量'),
        ),
        migrations.AddField(
            model_name='contest',
            name='silver_num',
            field=models.IntegerField(default=16, verbose_name='银奖数量'),
        ),
    ]
