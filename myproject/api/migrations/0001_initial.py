# Generated by Django 4.1.5 on 2023-03-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=6)),
                ('name_group', models.CharField(max_length=12)),
                ('url', models.CharField(max_length=60)),
            ],
        ),
    ]