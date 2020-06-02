# Generated by Django 3.0.2 on 2020-02-23 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField()),
                ('availability', models.PositiveIntegerField()),
                ('is_on_sale', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='market.Item')),
            ],
        ),
    ]
