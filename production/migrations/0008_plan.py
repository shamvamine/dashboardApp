# Generated by Django 5.0.3 on 2024-04-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_data_safetyperformance'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rom', models.FloatField()),
                ('milled_tonnes', models.FloatField()),
                ('gold', models.FloatField()),
                ('grade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dev_drilling', models.FloatField()),
                ('ore_gen', models.FloatField()),
            ],
        ),
    ]