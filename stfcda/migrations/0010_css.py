# Generated by Django 3.2.19 on 2023-11-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0009_todos'),
    ]

    operations = [
        migrations.CreateModel(
            name='css',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_title', models.CharField(max_length=200)),
                ('code', models.TextField()),
            ],
        ),
    ]
