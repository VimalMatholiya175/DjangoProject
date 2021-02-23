# Generated by Django 3.1.5 on 2021-02-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('outOfStock', models.BooleanField(default=False)),
                ('specialOffer', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='images/products')),
                ('pubDate', models.DateField()),
            ],
        ),
    ]
