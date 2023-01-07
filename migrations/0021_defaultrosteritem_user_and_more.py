# Generated by Django 4.1.4 on 2023-01-07 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lost_ark_checklist', '0020_defaultrosteritem_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultrosteritem',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lost_ark_checklist.user'),
        ),
        migrations.AlterField(
            model_name='defaultrosteritem',
            name='item_type',
            field=models.CharField(choices=[('WEEKLY', 'Weekly'), ('DAILY', 'Daily')], max_length=6),
        ),
    ]