# Generated by Django 4.1.5 on 2024-06-20 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0024_dept_spending'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept_spending_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('labour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('utilities', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stores', models.DecimalField(decimal_places=2, max_digits=10)),
                ('repairs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hauling', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loading', models.DecimalField(decimal_places=2, max_digits=10)),
                ('processing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('open_pit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('social_ammenities', models.DecimalField(decimal_places=2, max_digits=10)),
                ('security', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_overheads', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imtt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept_plan', to='production.departments')),
            ],
        ),
    ]