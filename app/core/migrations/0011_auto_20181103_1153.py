# Generated by Django 2.0.4 on 2018-11-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181013_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquery',
            name='pay_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='euro_list_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='euro_net_price',
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('rmb', '人民币'), ('eur', '欧元'), ('usd', '美元')], default='eur', max_length=10, verbose_name='币种'),
        ),
        migrations.AddField(
            model_name='product',
            name='list_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=20, verbose_name='面价'),
        ),
        migrations.AddField(
            model_name='product',
            name='net_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='折后价'),
        ),
    ]
