# Generated by Django 3.2.8 on 2024-02-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_announcetext_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorePDFs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(blank=True, upload_to='pdfs/')),
                ('boolval', models.IntegerField(default=0)),
            ],
        ),
    ]