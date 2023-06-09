# Generated by Django 4.0 on 2023-03-21 15:39

import core.watch_it.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_watch_it', '0014_contentpictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(upload_to=core.watch_it.models.content_picture_upload_path)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='core_watch_it.content')),
            ],
        ),
        migrations.DeleteModel(
            name='ContentPictures',
        ),
    ]
