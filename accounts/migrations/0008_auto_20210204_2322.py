# Generated by Django 3.1.4 on 2021-02-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210204_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
