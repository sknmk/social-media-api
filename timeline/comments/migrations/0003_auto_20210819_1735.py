# Generated by Django 3.2.5 on 2021-08-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0001_initial'),
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reactions',
            field=models.ManyToManyField(related_name='comments', through='reactions.UserReaction', to='reactions.Reaction'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
