# Generated by Django 3.2.9 on 2021-11-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('theme', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
