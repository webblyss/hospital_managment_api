# Generated by Django 4.2 on 2023-04-28 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OPD_', '0002_alter_opd_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_complains', models.TextField()),
                ('doctor_diagnosis', models.CharField(max_length=100)),
                ('medication', models.CharField(max_length=500)),
                ('admitted_to_ward', models.CharField(choices=[('FEMALE-WARD', 'FEMALE-WARD'), ('MALE-WARD', 'MALE-WARD'), ('PEADIATRIC-WARD', 'PEADIATRIC-WARD'), ('EMERGENCY-WARD', 'EMERGENCY-WARD')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD_.opd')),
            ],
        ),
    ]
