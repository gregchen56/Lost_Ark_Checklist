# Generated by Django 4.1.4 on 2023-01-04 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('lost_ark_checklist', '0005_user_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='session_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
        ),
    ]