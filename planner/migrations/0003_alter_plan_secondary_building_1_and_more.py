# Generated by Django 4.2.23 on 2025-07-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_plan_primary_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='secondary_building_1',
            field=models.CharField(choices=[('EM', 'Empty'), ('BA', 'Benedictine Abbey'), ('FM', 'Farm'), ('OR', 'Orchard'), ('PA', 'Pasture'), ('HN', 'Hunting'), ('FI', 'Fishing'), ('WD', 'Wood'), ('GD', 'Gold'), ('TN', 'Tin'), ('IN', 'Iron'), ('SL', 'Silver'), ('CP', 'Copper'), ('LD', 'Lead'), ('CL', 'Cloth'), ('SA', 'Salt'), ('BP', 'Beach Port'), ('PT', 'Pottery')], default='EM', max_length=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='secondary_building_2',
            field=models.CharField(choices=[('EM', 'Empty'), ('BA', 'Benedictine Abbey'), ('FM', 'Farm'), ('OR', 'Orchard'), ('PA', 'Pasture'), ('HN', 'Hunting'), ('FI', 'Fishing'), ('WD', 'Wood'), ('GD', 'Gold'), ('TN', 'Tin'), ('IN', 'Iron'), ('SL', 'Silver'), ('CP', 'Copper'), ('LD', 'Lead'), ('CL', 'Cloth'), ('SA', 'Salt'), ('BP', 'Beach Port'), ('PT', 'Pottery')], default='EM', max_length=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='secondary_building_3',
            field=models.CharField(choices=[('EM', 'Empty'), ('BA', 'Benedictine Abbey'), ('FM', 'Farm'), ('OR', 'Orchard'), ('PA', 'Pasture'), ('HN', 'Hunting'), ('FI', 'Fishing'), ('WD', 'Wood'), ('GD', 'Gold'), ('TN', 'Tin'), ('IN', 'Iron'), ('SL', 'Silver'), ('CP', 'Copper'), ('LD', 'Lead'), ('CL', 'Cloth'), ('SA', 'Salt'), ('BP', 'Beach Port'), ('PT', 'Pottery')], default='EM', max_length=2),
        ),
    ]
