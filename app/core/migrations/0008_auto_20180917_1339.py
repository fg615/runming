# Generated by Django 2.0.4 on 2018-09-17 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180531_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignment',
            name='shipment_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='发货日期'),
        ),
        migrations.AddField(
            model_name='consignment',
            name='shipment_type',
            field=models.CharField(choices=[('air', '空运'), ('see', '海运'), ('road', '公路'), ('other', '其他')], default='other', max_length=10, verbose_name='运输方式'),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='currency',
            field=models.CharField(blank=True, choices=[('rmb', '人民币'), ('eur', '欧元'), ('usd', '美元')], default='rmb', max_length=10, verbose_name='币种'),
        ),
    ]