# Generated by Django 4.1.4 on 2022-12-20 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lost_ark_checklist', '0003_rename_user_id_character_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RosterWeekly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lost_ark_checklist.user')),
            ],
        ),
        migrations.CreateModel(
            name='RosterDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lost_ark_checklist.user')),
            ],
        ),
    ]
