# Generated by Django 4.1 on 2022-09-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_act', '0006_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]