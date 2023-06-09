# Generated by Django 4.0 on 2023-03-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_watch_it', '0003_content_c_type_content_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('site', models.URLField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
