# Generated by Django 4.2.2 on 2023-06-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_alter_userdetail_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='contact',
            field=models.CharField(default='N/A', max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='height',
            field=models.FloatField(default='0', verbose_name='Height in Ft.'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='weight',
            field=models.FloatField(default='0', verbose_name=' Weight in Kg'),
        ),
    ]
