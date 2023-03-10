# Generated by Django 4.1.4 on 2022-12-25 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdiagnostic',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='records.patient'),
        ),
        migrations.AlterField(
            model_name='patientillness',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='illness', to='records.patient', verbose_name='Patient'),
        ),
    ]
