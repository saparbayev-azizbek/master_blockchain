# Generated by Django 5.0.4 on 2024-04-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=500)),
                ('izoh', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
