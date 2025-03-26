# Generated by Django 3.2.25 on 2025-03-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='hikes/')),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=500)),
            ],
        ),
    ]
