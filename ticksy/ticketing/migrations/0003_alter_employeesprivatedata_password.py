# Generated by Django 4.0.3 on 2022-04-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_tickets_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesprivatedata',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
