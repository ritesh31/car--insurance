# Generated by Django 3.0.5 on 2020-05-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mobile_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
