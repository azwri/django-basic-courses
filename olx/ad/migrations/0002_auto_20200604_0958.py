# Generated by Django 3.0.6 on 2020-06-04 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(limit_choices_to={'parents__isnull': True}, on_delete=django.db.models.deletion.CASCADE, related_name='add_category', to='ad.Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='code',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]