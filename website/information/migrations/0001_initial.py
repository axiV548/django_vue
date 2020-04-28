# Generated by Django 3.0.5 on 2020-04-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('标题', models.CharField(max_length=100, unique=True)),
                ('日期', models.DateField()),
                ('会场', models.CharField(blank=True, max_length=100)),
                ('出演', models.TextField()),
                ('详情', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'information',
                'db_table': 'information',
            },
        ),
    ]