# Generated by Django 5.0.7 on 2024-10-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0032_budget_recovery_plan_recovery_prod_budget_recovery'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='stock_pile',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]