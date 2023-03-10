# Generated by Django 4.1.3 on 2022-11-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobcart', '0004_alter_orders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
        migrations.AddField(
            model_name='orders',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
