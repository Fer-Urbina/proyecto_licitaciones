# Generated by Django 5.1.3 on 2024-11-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licitacion',
            name='presupuesto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]