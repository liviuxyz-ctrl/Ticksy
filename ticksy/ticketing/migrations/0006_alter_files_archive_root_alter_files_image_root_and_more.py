# Generated by Django 4.0.3 on 2022-05-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0005_alter_files_archive_root_alter_files_image_root_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='archive_root',
            field=models.FileField(null=True, upload_to='archives/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='image_root',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='pdf_root',
            field=models.FileField(null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
