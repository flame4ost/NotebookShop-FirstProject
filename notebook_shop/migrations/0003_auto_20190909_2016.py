# Generated by Django 2.2.5 on 2019-09-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook_shop', '0002_good_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(default='', upload_to='media/notebook_shop/good'),
        ),
    ]
