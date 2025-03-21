# Generated by Django 5.1.6 on 2025-03-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentMemoryModel',
            fields=[
                ('component_memory_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Memory ID')),
                ('component_memory_name', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Memory Name')),
                ('component_memory_producer', models.CharField(max_length=128, verbose_name='Memory Producer')),
                ('component_memory_model', models.CharField(max_length=128, verbose_name='Memory Model')),
                ('component_memory_type', models.CharField(choices=[('DDR', 'DDR'), ('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4')], max_length=32, verbose_name='Memory Type')),
                ('component_memory_size', models.PositiveIntegerField(verbose_name='Memory Size')),
                ('component_memory_clock_speed', models.PositiveIntegerField(verbose_name='Memory Clock Speed')),
                ('component_memory_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Memory Price')),
                ('component_memory_image', models.ImageField(default='default_memory.png', upload_to='components/memory', verbose_name='Memory Image')),
            ],
            options={
                'verbose_name': 'Memory Component',
                'verbose_name_plural': 'Memory Components',
                'unique_together': {('component_memory_producer', 'component_memory_model')},
            },
        ),
    ]
