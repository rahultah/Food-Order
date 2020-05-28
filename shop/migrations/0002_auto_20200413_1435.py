# Generated by Django 3.0.5 on 2020-04-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productCategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='productImage',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='productPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='productSubCategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
