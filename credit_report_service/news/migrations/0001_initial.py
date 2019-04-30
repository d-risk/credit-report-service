# Generated by Django 2.2 on 2019-04-30 04:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.UUIDField(db_index=True, editable=False)),
                ('title', models.TextField(db_index=True, editable=False)),
                ('date_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('snippet', models.TextField(editable=False)),
                ('url', models.URLField(editable=False)),
            ],
            options={
                'db_table': 'app_news',
                'ordering': ['-date_time'],
            },
        ),
    ]
