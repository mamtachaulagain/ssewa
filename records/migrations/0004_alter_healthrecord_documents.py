# Generated by Django 4.2.2 on 2023-06-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_healthrecord_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthrecord',
            name='documents',
            field=models.FileField(null=True, upload_to='healthrecords/'),
        ),
    ]
