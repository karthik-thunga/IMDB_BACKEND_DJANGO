# Generated by Django 4.0 on 2023-03-21 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_watch_it', '0011_rename_count_raing_content_count_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='certificate',
            field=models.CharField(choices=[('U', 'unrestricted public exhibition (U)'), ('U/A', 'parental guidance for children below age 12 (U/A)'), ('A', 'adult (A)'), ('S', 'viewing by specialised groups (S)')], default='U', max_length=5),
        ),
        migrations.AddField(
            model_name='content',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=60)),
        ),
    ]