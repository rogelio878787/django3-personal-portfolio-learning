# Generated by Django 3.0.5 on 2020-04-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200404_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Shirt', 'Shirt'), ('Sport Wear', 'Sport Wear'), ('Otwear', 'Outwear')], max_length=128),
        ),
    ]
