# Generated by Django 3.1.2 on 2020-11-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='Tax_Date',
            field=models.CharField(default='0.00', max_length=20),
        ),
    ]
