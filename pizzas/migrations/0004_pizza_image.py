# Generated by Django 3.0.5 on 2022-12-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
