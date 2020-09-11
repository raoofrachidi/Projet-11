# Generated by Django 3.0.8 on 2020-07-04 22:27

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
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('url', models.URLField()),
                ('picture', models.URLField()),
                ('nutriscore', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('picture_nutrition', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('picture', models.URLField()),
                ('nutriscore', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=250)),
                ('picture_nutrition', models.URLField(default='0000000')),
                ('favorite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Favorite')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
