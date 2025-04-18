# Generated by Django 5.1.6 on 2025-03-27 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
        ('components', '0006_delete_bookmark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildmodel',
            options={'ordering': ['-created_at'], 'verbose_name': 'Computer Build', 'verbose_name_plural': 'Computer Builds'},
        ),
        migrations.RemoveField(
            model_name='buildmodel',
            name='build_name',
        ),
        migrations.AlterField(
            model_name='buildmodel',
            name='cpu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.componentcpumodel'),
        ),
        migrations.AlterField(
            model_name='buildmodel',
            name='gpu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.componentgpumodel'),
        ),
        migrations.AlterField(
            model_name='buildmodel',
            name='memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.componentmemorymodel'),
        ),
    ]
