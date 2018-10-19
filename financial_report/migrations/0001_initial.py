# Generated by Django 2.1.2 on 2018-10-19 07:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=9, max_digits=99)),
            ],
            options={
                'db_table': 'app_financial_data',
            },
        ),
        migrations.CreateModel(
            name='FinancialRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=9, max_digits=99)),
            ],
            options={
                'db_table': 'app_financial_ratios',
            },
        ),
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.UUIDField(db_index=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('currency', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'app_financial_reports',
            },
        ),
        migrations.AddField(
            model_name='financialratio',
            name='financial_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financial_ratios', to='financial_report.FinancialReport'),
        ),
        migrations.AddField(
            model_name='financialdata',
            name='financial_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financial_data', to='financial_report.FinancialReport'),
        ),
    ]
