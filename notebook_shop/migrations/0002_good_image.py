# Generated by Django 2.2.5 on 2019-09-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='image',
            field=models.ImageField(default='', upload_to='notebook_shop/media/notebook_shop/good'),
        ),
    ]
