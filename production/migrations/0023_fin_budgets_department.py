# Generated by Django 4.1.5 on 2024-06-20 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0022_fin_budgets_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_budgets',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dept_cost', to='production.departments'),
            preserve_default=False,
        ),
    ]