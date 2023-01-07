# Generated by Django 4.1.4 on 2023-01-07 00:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost_ark_checklist', '0018_remove_chardaily_img_path_chardaily_img_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultRosterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('WEEKLY', 'Weekly'), ('DAILY', 'Daily')], max_length=6)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='chardaily',
            name='rested',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
