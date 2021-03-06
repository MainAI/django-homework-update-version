# Generated by Django 4.0.4 on 2022-04-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('image', models.TextField()),
                ('release_date', models.TextField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
    ]
