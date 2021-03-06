# Generated by Django 2.1.3 on 2018-12-03 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0004_auto_20181202_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='voted_users',
            field=models.ManyToManyField(related_name='vote_posts', through='collection.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('author', 'post')},
        ),
    ]
