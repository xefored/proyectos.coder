# Generated by Django 5.0.1 on 2024-02-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteles',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='descripciòn'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='precio',
            field=models.PositiveBigIntegerField(verbose_name='$'),
        ),
        migrations.AlterField(
            model_name='hoteles',
            name='precio',
            field=models.PositiveBigIntegerField(verbose_name='$'),
        ),
    ]