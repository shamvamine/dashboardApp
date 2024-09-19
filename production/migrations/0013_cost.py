# Generated by Django 4.1.5 on 2024-05-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0012_trammings_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('c1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c1_cash_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c2_cash_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c3_cash_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
