# Generated by Django 5.1.3 on 2024-11-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khayyat', '0004_alter_order_deposit_alter_order_wage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deposit',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='بیعانه(تومان)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='wage',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='اجرت(تومان)'),
        ),
    ]
