# Generated by Django 3.0.13 on 2021-12-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection_search', '0002_auto_20210928_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='soundcloud_link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]